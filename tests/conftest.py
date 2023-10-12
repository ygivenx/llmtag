import pytest
import pandas as pd


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
    data = pd.read_csv("benchmark_data/gpt_sim.csv")
    labels = data.label.tolist()
    notes = data.notes.tolist()
    yield zip(notes, labels)
