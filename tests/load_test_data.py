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
<<<<<<< HEAD
=======

def load_simulation_df1():
    '''
    :return pd.DataFrame that contains sim data
    '''
    return load_data_file('df_simulation1.csv')

def load_gpt_sim():
    '''
    :return pd.DataFrame that contains gpt sim data
    '''
    return load_data_file('gpt_sim.csv')

def load_gpt_sim_small():
    '''
    :return pd.DataFrame that contains gpt sim small data
    '''
    return load_data_file('gpt_sim_small.csv')

def load_labeled_df1():
    '''
    Load LLM-labeled simulation data
    '''
    return load_data_file('out.csv')
>>>>>>> fe4a403 (Condense loading data to single function and make changes in tests, rebase on Rohans changes)
