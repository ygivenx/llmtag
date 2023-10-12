import os
import pathlib

import pandas as pd

# Note: after speaking with Dan, can host data online on dropbox/s3/googledrive and pull using python script

def load_data_file(filename):
    file_path = os.path.join(os.path.dirname(__file__), f'benchmark_data/{filename}')
    with open(file_path, 'r') as f:
        return pd.read_csv(f, encoding='latin-1')

def load_simulation_df1():
    '''
    Load Simulation Data For Binary Endpoints DCA
    :return pd.DataFrame that contains binary data
    '''
    return load_data_file('df_simulation1.csv')
