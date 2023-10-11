import os
from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()

model_path = os.getenv("MODEL")

llm = Llama(model_path=model_path)
output = llm("Q: What is the capital of France? A: ", max_tokens=5, stop=["Q:", "\n"], echo=True)
print(output)
print(output["choices"][0]["text"])