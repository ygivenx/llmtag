import os
import pandas as pd

from .load_test_data import load_data_file  # Import the new function

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
