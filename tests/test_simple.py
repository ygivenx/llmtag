import pytest
import os
from dotenv import load_dotenv
from llmtag.llm_label import get_note_label

from .load_test_data import load_simulation_df1

load_dotenv()


model_path = os.getenv("MODEL")


def test_load_simdata1():
    print('\n', load_simulation_df1())


def test_llm_simple_prompt(note):
    res = get_note_label(note, n_ctx=256)
    assert int(res["label"]) == 1


def test_multiple_notes(notes):
    res =  get_note_label(notes[0])
    assert int(res["label"]) == int(notes[1])
