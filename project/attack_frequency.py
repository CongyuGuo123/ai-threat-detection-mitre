import pandas as pd
from collections import Counter

# Load y_test labels
y_test = pd.read_csv('dataset/y_test.csv')['Label']

# Count label frequency
label_counts = Counter(y_test)

# Load mapping file
mapping_df = pd.read_csv('attack_to_mitre_mapping.csv')

# Build label-to-technique mapping (label 1 -> row 0, etc.)
label_to_technique = {i: mapping_df.iloc[i - 1]['Technique ID'] for i in range(1, 15)}

print("Label\tTechnique ID\tFrequency")
for label, count in sorted(label_counts.items()):
    if label == 0:
        continue
    technique_id = label_to_technique.get(label, "UNKNOWN")
    print(f"{label}\t{technique_id}\t{count}")
