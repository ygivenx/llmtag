"""
Interface to llama for labeling notes

TODO: add all parameters for llama_cpp
"""
import os
from dotenv import load_dotenv
from llama_cpp import Llama, LlamaGrammar
import httpx
import json

load_dotenv()
 
model_path = os.getenv("MODEL")


def get_note_label(note, n_threads=4, n_batch=32, n_ctx=512, **kwargs):
    """
    note: str
    n_ctx: int (default=512) - context length
    kwargs: dict - additional arguments to llama_cpp.Llama.__call__
    """
    llm = Llama(model_path=model_path,
                n_threads=n_threads,
                n_batch=n_batch,
                n_ctx=n_ctx)
    
    grammar_text = httpx.get("https://raw.githubusercontent.com/ggerganov/llama.cpp/master/grammars/json.gbnf").text
    grammar = LlamaGrammar.from_string(grammar_text)
    prompt = """


    Is there an evidence of deep venous thrombosis or pulmonary embolism in the note above?
    Provide the result in a json format {label: 0/1, reason: "short explanation"}

    Note:
    Patient complains of leg pain and swelling. Ultrasound confirms DVT

    output: {"reason": "Ultrasound confirms DVT", "label": 1}

    Note:
    Patient has a history of DVT. No current symptoms noted.

    output: {"reason": "Historical DVT", "label": 0}
    """

    tokenized_note = note.split()
    if len(tokenized_note) < n_ctx - 60:
        note = " ".join(tokenized_note)
    else:
        note = " ".join(tokenized_note[:n_ctx - 60])
    
    # return {"reason": "dvt", "label": 1}
    print(note)
    response = llm(note + prompt,
                max_tokens=-1,
                repeat_penalty=1.0,
                temperature=0.1,
                grammar=grammar,
                echo=False,
                **kwargs)
                #  stop=["Q:", "\n"])

    try:
        res = json.loads(response['choices'][0]['text'])
    except json.JSONDecodeError:
        return {"label": "NA", "reason": response['choices'][0]['text']}

    return res
