import pytest
import os
from dotenv import load_dotenv
from llmtag.llm_label import get_note_label

load_dotenv()


model_path = os.getenv("MODEL")


def test_llm_simple_prompt(note):
    res = get_note_label(note, n_ctx=256)
    assert res["label"].lower() == "yes"


def test_multiple_notes(notes):
    for note in notes:
        res = get_note_label(note, n_ctx=256)
        assert res["label"].lower() == "yes"