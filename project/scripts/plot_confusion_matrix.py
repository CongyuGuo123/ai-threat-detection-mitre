import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import joblib
import os

# Paths
X_test_path = os.path.join("dataset", "X_test.csv")
y_test_path = os.path.join("dataset", "y_test.csv")
model_path = os.path.join("trainedModel", "random_forest_model.pkl")

# Load test data
X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path).values.ravel()

# Load trained model
model = joblib.load(model_path)

# Make predictions
y_pred = model.predict(X_test)

# Class labels (based on your dataset)
labels = [
    'BENIGN', 'Bot', 'DDoS', 'DoS GoldenEye', 'DoS Hulk',
    'DoS Slowhttptest', 'DoS slowloris', 'FTP-Patator', 'SSH-Patator',
    'Web Attack – Brute Force', 'Web Attack – Sql Injection',
    'Web Attack – XSS', 'Infiltration', 'PortScan', 'Heartbleed'
]

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Visualize the confusion matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues',
            xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix (Random Forest)")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("confusion_matrix_heatmap.png", dpi=300)
plt.show()
