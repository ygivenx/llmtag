import os
import pandas as pd

def load_data_file(file_type):
    filenames = {
        'df_simulation1.csv': 'df_simulation1.csv',
        'gpt_sim.csv': 'gpt_sim.csv',
        'gpt_sim_small.csv': 'gpt_sim_small.csv',
        'out.csv': 'out.csv'
    }
    
    filename = filenames.get(file_type)
    if filename is None:
        raise ValueError("Invalid file_type specified")
        
    file_path = os.path.join(os.path.dirname(__file__), f'benchmark_data/{filename}')
    with open(file_path, 'r') as f:
        return pd.read_csv(f, encoding='latin-1')
