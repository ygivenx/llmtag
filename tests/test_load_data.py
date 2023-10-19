import os
import pandas as pd

from .load_test_data import load_data_file  # Import the new function

model_path = os.path.join(os.getcwd(), 'models/7B/llama-2-7b-chat.Q4_K_M.gguf')

def test_model_path_exists():
    print(model_path)
    assert os.path.exists(model_path)

def test_load_simdata1():
    df = load_data_file('df_simulation1.csv')  # Use the new function with the appropriate argument
    assert isinstance(df, pd.DataFrame)  # Check if it's a DataFrame
    assert df.shape[0] == 50  # Check if it has 50 rows
    assert 'notes' in df.columns  # Check if 'notes' column exists
    assert 'label' in df.columns  # Check if 'label' column exists

# Uncomment and modify other tests as needed
# def test_load_labeled_simdata1():
#     df = load_data_file('labeled_df1')
#     ...

# def test_llm_simple_prompt(note):
#     ...

# def test_multiple_notes(notes):
#     ...
