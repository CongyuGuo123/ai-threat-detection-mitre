import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load test labels
y_test = pd.read_csv('dataset/y_test.csv')['Label']

# Count frequency of each label
label_counts = Counter(y_test)

# Load attack-to-technique mapping
mapping_df = pd.read_csv('attack_to_mitre_mapping.csv')

# Build label-to-attack name and technique ID mapping (skip label 0 = BENIGN)
label_to_info = {
    i: (mapping_df.iloc[i - 1]['Attack Name'], mapping_df.iloc[i - 1]['Technique ID'])
    for i in range(1, 15)
}

# Build frequency DataFrame
data = []
for label, count in sorted(label_counts.items()):
    if label == 0:
        continue
    attack_name, technique_id = label_to_info[label]
    data.append({
        'Attack Name': attack_name,
        'Technique ID': technique_id,
        'Frequency': count
    })

df = pd.DataFrame(data)

# --- Bar Chart: Technique ID vs Frequency ---
plt.figure(figsize=(12, 6))
barplot = sns.barplot(
    x='Technique ID',
    y='Frequency',
    data=df,
    palette='viridis',
    errorbar=None  # Remove confidence interval line
)

# Add value labels on top of each bar
for bar in barplot.patches:
    barplot.annotate(
        format(bar.get_height(), '.0f'),
        (bar.get_x() + bar.get_width() / 2., bar.get_height()),
        ha='center', va='bottom',
        fontsize=9
    )

plt.title("Technique ID vs Frequency")
plt.xlabel("Technique ID")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Technique_Bar_Chart.png", dpi=300, bbox_inches='tight')
plt.close()

# --- Heatmap: Attack Name vs Frequency ---
plt.figure(figsize=(10, 6))
heatmap_df = df[['Attack Name', 'Frequency']].set_index('Attack Name')

# Create a horizontal heatmap using seaborn
sns.heatmap(
    heatmap_df,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    linewidths=0.5,
    cbar=True
)

plt.title("Attack Frequency Heatmap (by Attack Name)")
plt.xlabel("Frequency")
plt.ylabel("Attack Name")
plt.tight_layout()
plt.savefig("Attack_Heatmap.png", dpi=300, bbox_inches='tight')
plt.close()
