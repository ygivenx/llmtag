import pytest
import os
from dotenv import load_dotenv
from llama_cpp import Llama

load_dotenv()


model_path = os.getenv("MODEL")


def test_llm_simple_prompt(note):
    llm = Llama(model_path=model_path,  n_threads=4)
    n_ctx = 512
    output = llm(" ".join(note.split()[:n_ctx-32]),
                max_tokens=32,
                repeat_penalty=1.0,
                #  stop=["Q:", "\n"],
                echo=True)
    assert "yes" in output["choices"][0]["text"].lower()


def test_multiple_notes(notes):
    llm = Llama(model_path=model_path,  n_threads=4)
    n_ctx = 512

    for note in notes:
        output = llm(" ".join(note.split()[:n_ctx-32]),
                max_tokens=32,
                repeat_penalty=1.0,
                #  stop=["Q:", "\n"],
                echo=True)
        assert "yes" in output["choices"][0]["text"].lower()