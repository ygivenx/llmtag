import pandas as pd
import random
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path for the CSV file
csv_path = os.path.join(current_directory, 'df_simulation1.csv')

# Define possible text fragments related to VTE
positive_fragments = [
    "Thrombus present",
    "Deep venous thrombosis present",
    "Few new pulmonary emboli",
    "Segmental and subsegmental pulmonary artery branches",
    "Central saddle pulmonary embolus",
    "Right-sided heart strain",
    "Right ventricular to left ventricular ratio is 0.8"
]

# Define possible text fragments not related to VTE
negative_fragments = [
    "No thrombus",
    "Decreased left pulmonary artery emboli",
    "The remaining lung parenchyma is unchanged",
    "No right-sided heart strain",
    "No central saddle pulmonary embolus"
]

# Initialize empty lists to hold notes and labels
notes = []
labels = []

# Generate 50 rows
for _ in range(50):
    note_fragments = []
    label = 0  # Assume negative by default

    # Randomly select fragments to form a note
    while True:
        fragment = random.choice(positive_fragments + negative_fragments)
        if len(", ".join(note_fragments) + fragment) + len("FINDINGS: ") < 100:
            note_fragments.append(fragment)
            if fragment in positive_fragments:
                label = 1
        else:
            break

    # Create the note
    note = "FINDINGS: " + ", ".join(note_fragments)

    # Append the generated note and label to lists
    notes.append(note)
    labels.append(label)

# Create a DataFrame
df = pd.DataFrame({
    'Notes': notes,
    'VTE_Label': labels
})

df.to_csv(csv_path, index=False)