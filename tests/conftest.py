import pytest

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
    labels = [1, 0]
    notes = [one_note, one_note]
    for note, label in zip(notes, labels):
        yield note, label
