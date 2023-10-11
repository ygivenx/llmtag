from .llm_label import get_note_label

def main():
    note = """
    FINDINGS:

    PULMONARY EMBOLUS: Few new pulmonary emboli within segmental and 
    subsegmental pulmonary artery branches in the left lower lobe. No central 
    saddle pulmonary embolus. No right-sided heart strain. Right ventricular 
    to left ventricular ratio is 0.8.

    Provide the Is there an evidence of deep venous thrombosis or pulmonary embolism in the note above?
    Provide a json list of all evidence in the json format with the following fields:
    reason: reason for the evidence
    label: label of the evidence (yes/no)
    """
    res = get_note_label(note)


if __name__ == "__main__":
    main()
