# scripts/evaluateModel.py

import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os
import csv
from sklearn.metrics import classification_report

X_test_path = os.path.join("dataset", "X_test.csv")
y_test_path = os.path.join("dataset", "y_test.csv")


X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path).values.ravel() 

model_path = os.path.join("trainedModel", "random_forest_model.pkl")

model = joblib.load(model_path)

y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

report_dict = classification_report(y_test, y_pred, output_dict=True)

with open("evaluation_results.csv", mode="w", newline="") as file:
   writer = csv.writer(file)
   writer.writerow(["Class", "Precision", "Recall", "F1-Score", "Support"])
   for label, metrics in report_dict.items():
        if isinstance(metrics, dict):
            writer.writerow([
                label,
                round(metrics["precision"], 4),
                round(metrics["recall"], 4),
                round(metrics["f1-score"], 4),
                int(metrics["support"])
            ])