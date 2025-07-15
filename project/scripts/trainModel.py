import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def load_preprocessed_data():
    # Load datasets from the dataset folder
    X_train = pd.read_csv('dataset/X_train.csv').values
    X_test = pd.read_csv('dataset/X_test.csv').values
    y_train = pd.read_csv('dataset/y_train.csv')['Label'].values
    y_test = pd.read_csv('dataset/y_test.csv')['Label'].values
    label_encoder = joblib.load('dataset/label_encoder.pkl')
    scaler = joblib.load('dataset/scaler.pkl')
    feature_names = pd.read_csv('dataset/X_train.csv').columns
    return X_train, X_test, y_train, y_test, label_encoder, scaler, feature_names


def train_random_forest(X_train, y_train):
    # Initialize and train Random Forest model
    model = RandomForestClassifier(
        n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'trainedModel/random_forest_model.pkl')
    return model


if __name__ == "__main__":
    # Load preprocessed data
    X_train, X_test, y_train, y_test, label_encoder, scaler, feature_names = load_preprocessed_data()

    # Train Random Forest model
    print("Training Random Forest model...")
    rf_model = train_random_forest(X_train, y_train)
    print("Random Forest model trained and saved as 'dataset/random_forest_model.pkl'")

    # Print dataset shapes for verification
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
