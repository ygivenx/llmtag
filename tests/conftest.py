import pytest
import pandas as pd

from .load_test_data import load_data_file

one_note = """
            FINDINGS:

            PULMONARY EMBOLUS: Few new pulmonary emboli within segmental and 
            subsegmental pulmonary artery branches in the left lower lobe. No central 
            saddle pulmonary embolus. No right-sided heart strain. Right ventricular 
            to left ventricular ratio is 0.8.
        """

@pytest.fixture
def note():
    yield one_note

@pytest.fixture
def notes():
<<<<<<< HEAD
    data = load_data_file('df_simulation1.csv').sample(10, random_state=42)
=======
    data = load_simulation_df1().sample(10, random_state=42)
>>>>>>> fe4a403 (Condense loading data to single function and make changes in tests, rebase on Rohans changes)
    labels = data.label.tolist()
    notes = data.notes.tolist()
    yield zip(notes, labels)

