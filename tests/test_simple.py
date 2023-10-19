import json
import pytest
from unittest.mock import patch
# from .load_test_data import load_data_file  # Import the new function

def mock_get_note_label_for_single(*args, **kwargs):
    return {'choices': [{'text': json.dumps({'label': "1", 'reason': "Test reason"})}]}

@patch('llmtag.llm_label.get_note_label', side_effect=mock_get_note_label_for_single)
def test_llm_simple_prompt(mocked_get_note_label):
    one_note = "FINDINGS: PULMONARY EMBOLUS: Few new pulmonary emboli..."
    model_path = 'mock_model_path'
    res = mocked_get_note_label(note=one_note, model_path=model_path, n_ctx=512)
    assert json.loads(res['choices'][0]['text'])['label'] == "1"

def mock_get_note_label_for_multiple(*args, **kwargs):
    note_text = kwargs.get('note', '')
    phrases = ["Deep venous thrombosis present", "Central saddle pulmonary embolus", "Right-sided heart strain", "Thrombus present", "Few new pulmonary emboli"]
    label = "1" if any(phrase in note_text for phrase in phrases) else "0"
    return {'choices': [{'text': json.dumps({'label': label, 'reason': "Test reason"})}]}

@patch('llmtag.llm_label.get_note_label', side_effect=mock_get_note_label_for_multiple)
def test_multiple_notes(mocked_get_note_label, notes):
    for note, label in notes:
        res = mocked_get_note_label(note=note, model_path='mock_model_path', n_ctx=512)
        returned_label = int(json.loads(res['choices'][0]['text'])['label'])
        assert returned_label == label


