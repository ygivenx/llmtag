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

    response = llm(" ".join(note.split()[:n_ctx-32]),
                max_tokens=-1,
                repeat_penalty=1.0,
                temperature=0.0,
                grammar=grammar,
                **kwargs)
                #  stop=["Q:", "\n"])

    try:
        res = json.dumps(json.loads(response['choices'][0]['text']), indent=4)
    except json.JSONDecodeError:
        res = response['choices'][0]['text']

    print(res)
    return res
