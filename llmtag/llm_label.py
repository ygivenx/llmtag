"""
Interface to llama for labeling notes.

This module provides an interface to the llama library for labeling medical notes.
It fetches a grammar definition from a remote URL and uses it to interpret the
output from the llama model. The main function `get_note_label` takes a medical
note and returns a label and reason based on the content of the note.

TODO: Add all parameters for llama_cpp
"""

import os
import json
from typing import Dict, Any
from dotenv import load_dotenv
from llama_cpp import Llama, LlamaGrammar
import httpx

def get_note_label(note: str, model_path: str, n_threads: int = 4, n_batch: int = 32, n_ctx: int = 512, **kwargs: Any) -> Dict[str, Any]:
    """
    Label a medical note using the llama model.

    Parameters:
    - note (str): The medical note to be labeled.
    - model_path (str): Path to the llama model.
    - n_threads (int, optional): Number of threads for llama. Defaults to 4.
    - n_batch (int, optional): Batch size for llama. Defaults to 32.
    - n_ctx (int, optional): Context length for llama. Defaults to 512.
    - **kwargs: Additional keyword arguments for llama.

    Returns:
    - Dict[str, Any]: A dictionary containing the label and reason.
    """
    
    llm = Llama(model_path=model_path,
                n_threads=n_threads,
                n_batch=n_batch,
                n_ctx=n_ctx, verbose=False)

    grammar_text = httpx.get("https://raw.githubusercontent.com/ggerganov/llama.cpp/master/grammars/json.gbnf").text
    grammar = LlamaGrammar.from_string(grammar_text, verbose=False)

    tokenized_note = note.split()
    truncated_note = " ".join(tokenized_note[:min(len(tokenized_note), n_ctx - 60)])

    prompt = f"""
    Is there evidence of deep venous thrombosis or pulmonary embolism in the note?
    Generate output as shown in examples below with labels as 0/1 and a brief reason.

    Note:
    {truncated_note}

    Output:
    """

    response = llm(prompt,
                   max_tokens=-1,
                   repeat_penalty=1.0,
                   temperature=0.0,
                   grammar=grammar,
                   echo=False,
                   stop=["Note:\n", "\n"],
                   **kwargs)

    try:
        res = json.loads(response['choices'][0]['text'])
        res.setdefault("label", "NA")
        res.setdefault("reason", "NA")
    except json.JSONDecodeError:
        return {"label": "NA", "reason": response['choices'][0]['text']}

    return res
