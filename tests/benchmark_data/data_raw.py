import csv
import random
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the path for the CSV file
csv_path = os.path.join(current_directory, 'simulation_dataset.csv')

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

# Combine both positive and negative fragments
all_fragments = positive_fragments + negative_fragments

# Open CSV file for writing
with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header
    csvwriter.writerow(['Notes'])
    
    # Generate 50 rows
    for _ in range(50):
        # Randomly select fragments to form a note
        note = "FINDINGS: "
        while len(note) < 100:
            fragment = random.choice(all_fragments)
            if len(note) + len(fragment) + 2 <= 100:  # +2 for possible ", "
                note += fragment
                if len(note) < 98:  # 98 to leave room for ", "
                    note += ", "
                    
        # Write the generated note to the CSV
        csvwriter.writerow([note])
