import pytest

one_note = """
            FINDINGS:

            PULMONARY EMBOLUS: Few new pulmonary emboli within segmental and 
            subsegmental pulmonary artery branches in the left lower lobe. No central 
            saddle pulmonary embolus. No right-sided heart strain. Right ventricular 
            to left ventricular ratio is 0.8.

            Q: Is there an evidence of deep venous thrombosis or pulmonary embolism in the note above?
            A: 
        """

@pytest.fixture
def note():
    yield one_note

@pytest.fixture
def notes():
    yield [one_note, one_note]
