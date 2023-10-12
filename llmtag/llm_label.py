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
                n_ctx=n_ctx, verbose=False)

    grammar_text = httpx.get("https://raw.githubusercontent.com/ggerganov/llama.cpp/master/grammars/json.gbnf").text
    grammar = LlamaGrammar.from_string(grammar_text, verbose=False)

    tokenized_note  = note.split()
    if len(tokenized_note) < n_ctx - 60:
        note = " ".join(tokenized_note)
    else:
        note = " ".join(tokenized_note[:n_ctx - 60])

    prompt = f"""
    Is there an evidence of deep venous thrombosis or pulmonary embolism in the note?
    Generate output as shown in examples below with labels as 0/1 and a  brief reason.

    Note:
    Patient complains of leg pain and swelling. Ultrasound confirms DVT

    output: {{'reason': 'Ultrasound confirms DVT', 'label': 1}}

    Note:
    Patient has a history of DVT. No current symptoms noted

    output: {{'reason': 'No Symptoms found', 'label': 0}}
    
    Note:
    {note}

    Output:
    """

    print("###########################")
    print(note)
    response = llm(prompt,
                max_tokens=-1,
                repeat_penalty=1.0,
                temperature=0.0,
                grammar=grammar,
                echo=False,
               stop=["Note:\n", "\n"],
                **kwargs,
                )

    try:
        res = json.loads(response['choices'][0]['text'])
        print(res)
        if "label" not in res.keys():
            res["label"] = "NA"
        if "reason" not in res.keys():
            res["reason"] = "NA"
    except json.JSONDecodeError:
        return {"label": "NA", "reason": response['choices'][0]['text']}

    print(res)
    return res
