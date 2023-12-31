__version__ = '0.1.0'

"""
Labeling txt in python

Modules exported by this package:

- `get_note_label`
- `load_test_data`

"""

from dotenv import load_dotenv
from llama_cpp import Llama, LlamaGrammar
import httpx
import json

from llmtag import load_test_data
from llmtag.llm_label import get_note_label
from llmtag.download_weights import download_llama_weights
import os

data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

load_dotenv()
 
model_path = os.getenv("MODEL")