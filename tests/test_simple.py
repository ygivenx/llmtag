import pytest
import json
import os
from dotenv import load_dotenv
from llmtag.llm_label import get_note_label

from .load_test_data import load_simulation_df1, load_labeled_df1, load_gpt_sim, load_gpt_sim_small

load_dotenv()

model_path = os.getenv("MODEL")

def test_load_simdata1():
    print('\n', load_simulation_df1())

def test_load_labeled_simdata1():
    print('\n', load_labeled_df1().values)

def test_llm_simple_prompt(note):
    res = get_note_label(note = note, n_ctx=512)
    assert int(res["label"]) == 1

# def test_multiple_notes(notes):
#     for note, label in notes:
#         res = get_note_label(note, n_ctx=512)
#         if res['label'] == 'NA':
#             assert label == 0
#         else:
#             assert res["label"] == label
