import os
from dotenv import load_dotenv
from llama_cpp import Llama, LlamaGrammar
import httpx
import json

load_dotenv()
 
model_path = os.getenv("MODEL")

llm = Llama(model_path=model_path,  n_threads=1, n_batch=1)
n_ctx = 512
note = """
FINDINGS:

PULMONARY EMBOLUS: Few new pulmonary emboli within segmental and 
subsegmental pulmonary artery branches in the left lower lobe. No central 
saddle pulmonary embolus. No right-sided heart strain. Right ventricular 
to left ventricular ratio is 0.8.

Provide the Is there an evidence of deep venous thrombosis or pulmonary embolism in the note above?
Provide a json list of all evidence in the json format with the following fields:
reason: reason for the evidence
label: label of the evidence (yes/no)
"""

grammar_text = httpx.get("https://raw.githubusercontent.com/ggerganov/llama.cpp/master/grammars/json.gbnf").text
grammar = LlamaGrammar.from_string(grammar_text)

output = llm(" ".join(note.split()[:n_ctx-32]),
             max_tokens=-1,
             repeat_penalty=1.0,
             temperature=0.0,
             grammar=grammar)
            #  stop=["Q:", "\n"])

print(output)
