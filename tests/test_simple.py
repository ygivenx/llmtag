import os
import httpx
from llama_cpp import Llama, LlamaGrammar

from llmtag.llm_label import get_note_label
from .load_test_data import load_simulation_df1, load_labeled_df1, load_gpt_sim, load_gpt_sim_small

from unittest.mock import patch, MagicMock
import json
import pytest

def mock_get_note_label(*args, **kwargs):
    return {'choices': [{'text': json.dumps({'label': "1", 'reason': "Test reason"})}]}

@patch('llmtag.llm_label.get_note_label', side_effect=mock_get_note_label)
def test_llm_simple_prompt(mocked_get_note_label):
    one_note = """
            FINDINGS:
            PULMONARY EMBOLUS: Few new pulmonary emboli within segmental and
            subsegmental pulmonary artery branches in the left lower lobe. No central
            saddle pulmonary embolus. No right-sided heart strain. Right ventricular
            to left ventricular ratio is 0.8.
        """
    model_path = 'mock_model_path'
    res = mocked_get_note_label(note=one_note, model_path=model_path, n_ctx=512)

    assert json.loads(res['choices'][0]['text'])['label'] == "1"
    assert json.loads(res['choices'][0]['text'])['reason'] == "Test reason"

def mock_get_note_label(*args, **kwargs):
    note_text = kwargs.get('note', '')
    if any(phrase in note_text for phrase in ["Deep venous thrombosis present", "Central saddle pulmonary embolus", "Right-sided heart strain", "Thrombus present", "Few new pulmonary emboli"]):
        return {'choices': [{'text': json.dumps({'label': "1", 'reason': "Test reason"})}]}
    else:
        return {'choices': [{'text': json.dumps({'label': "0", 'reason': "Test reason"})}]}

@patch('llmtag.llm_label.get_note_label', side_effect=mock_get_note_label)
def test_multiple_notes(mocked_get_note_label, notes):
    for note, label in notes:
        res = mocked_get_note_label(note=note, model_path='mock_model_path', n_ctx=512)
        returned_label = json.loads(res['choices'][0]['text'])['label']
        if int(returned_label) != label:
            print(f"Note: {note}")
            print(f"Returned label: {returned_label}")
            print(f"Expected label: {label}")
        assert int(returned_label) == label

