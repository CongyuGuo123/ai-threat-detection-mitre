import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os


# Load the CICIDS2017 dataset
def load_dataset():
    file_paths = [
        'dataset/Monday-WorkingHours.pcap_ISCX.csv',
        'dataset/Tuesday-WorkingHours.pcap_ISCX.csv',
        'dataset/Wednesday-WorkingHours.pcap_ISCX.csv',
        'dataset/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv',
        'dataset/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv',
        'dataset/Friday-WorkingHours-Morning.pcap_ISCX.csv',
        'dataset/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv',
        'dataset/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv'
    ]
    df_list = [pd.read_csv(file) for file in file_paths]
    df = pd.concat(df_list, ignore_index=True)
    return df


# Clean and preprocess the dataset
def preprocess_dataset(df):
    # Remove leading/trailing spaces in column names
    df.columns = df.columns.str.strip()
    # Replace infinite values with NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    # Drop rows with NaN or missing values
    df.dropna(inplace=True)
    # Remove duplicates
    # df.drop_duplicates(inplace=True)
    # Encode labels (Benign vs. Attack types)
    label_encoder = LabelEncoder()
    df['Label'] = label_encoder.fit_transform(df['Label'])
    # Define features (X) and target (y)
    X = df.drop('Label', axis=1)
    y = df['Label']
    # Normalize numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Split into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, label_encoder, scaler, df.columns


# Save datasets and objects to the dataset folder
def save_datasets(X_train, X_test, y_train, y_test, label_encoder, scaler, feature_names):
    # Convert arrays to DataFrames for saving
    # Exclude 'Label' column
    X_train_df = pd.DataFrame(X_train, columns=feature_names[:-1])
    X_test_df = pd.DataFrame(X_test, columns=feature_names[:-1])
    y_train_df = pd.DataFrame(y_train, columns=['Label'])
    y_test_df = pd.DataFrame(y_test, columns=['Label'])

    # Save to CSV files
    X_train_df.to_csv('dataset/X_train.csv', index=False)
    X_test_df.to_csv('dataset/X_test.csv', index=False)
    y_train_df.to_csv('dataset/y_train.csv', index=False)
    y_test_df.to_csv('dataset/y_test.csv', index=False)

    # Save label encoder and scaler
    joblib.dump(label_encoder, 'dataset/label_encoder.pkl')
    joblib.dump(scaler, 'dataset/scaler.pkl')

    print("Datasets and objects saved to 'dataset' folder!")


# Main function to call functions
if __name__ == "__main__":
    df = load_dataset()
    X_train, X_test, y_train, y_test, label_encoder, scaler, feature_names = preprocess_dataset(
        df)
    save_datasets(X_train, X_test, y_train, y_test,
                  label_encoder, scaler, feature_names)
    print("Dataset preprocessed successfully!")
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    print("Label distribution:", pd.Series(
        label_encoder.inverse_transform(y_train)).value_counts())
