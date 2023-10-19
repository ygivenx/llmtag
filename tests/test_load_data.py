import os
import pandas as pd

from .load_test_data import load_simulation_df1

model_path = os.getcwd()+ '/models/7B/ggml-vocab-llama.gguf'

def test_model_path_exists():
    assert os.path.exists(model_path)

def test_load_simdata1():
    df = load_simulation_df1()
    assert isinstance(df, pd.DataFrame)  # Check if it's a DataFrame
    assert df.shape[0] == 50  # Check if it has 50 rows
    assert 'notes' in df.columns  # Check if 'notes' column exists
    assert 'label' in df.columns  # Check if 'label' column exists

# def test_load_labeled_simdata1():
#     print('\n', load_labeled_df1())

# def test_llm_simple_prompt(note):
#     res = get_note_label(note, model_path = model_path, n_ctx=512)

#     print(res)q
#     print('\n')
#     print('\n')
#     assert int(res["label"]) == 1

# def test_multiple_notes(notes):
#     for note, label in notes:
#         res = get_note_label(note, model_path = model_path, n_ctx=512)
#         if res['label'] == 'NA':
#             assert label == 0
#         else:
#             assert res["label"] == label
