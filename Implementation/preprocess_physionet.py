import pandas as pd
import numpy as np
import os
import glob
from sklearn.preprocessing import StandardScaler

def preprocess_patient_file(file_path, scaler=None, fit_scaler=False):
    """
    Loads a single patient's .psv file, handles missing ICU data logically,
    and returns normalized features and labels.
    """
    # Load raw data
    df = pd.read_csv(file_path, sep='|')
    
    # 1. Imputation Strategy
    # Forward-fill (ffill): Carry the last known medical value forward in time
    df = df.ffill()
    
    # Backward-fill (bfill): If the first few hours are missing, fill them with the first recorded value
    df = df.bfill()
    
    # Zero-fill: If the patient NEVER had a particular lab test done, default it to 0
    df = df.fillna(0)
    
    # 2. Feature and Label Extraction
    y = df['SepsisLabel'].values
    X = df.drop(columns=['SepsisLabel']).values
    
    # 3. Normalization (Only fit on training data, apply to all)
    if fit_scaler and scaler is not None:
        scaler.partial_fit(X)
    elif scaler is not None:
        X = scaler.transform(X)
        
    return X, y

def build_federated_dataset(data_dir, max_patients_to_process=100):
    """
    Simulates preparing the PhysioNet dataset for a specific Federated Node.
    """
    print(f"[*] Scanning directory: {data_dir}")
    all_psv_files = glob.glob(os.path.join(data_dir, '*.psv'))
    
    if len(all_psv_files) == 0:
        print("[!] No .psv files found. Check your directory path.")
        return
        
    print(f"[*] Found {len(all_psv_files)} patients.")
    
    # Focus on a subset for rapid evaluation/demo bounds
    files_to_process = all_psv_files[:max_patients_to_process]
    print(f"[*] Preprocessing a sample batch of {len(files_to_process)} ICU patients...")
    
    global_scaler = StandardScaler()
    
    processed_X = []
    processed_y = []
    
    # Pass 1: Fit Scaler and Extract
    for psv_file in files_to_process:
        X, y = preprocess_patient_file(psv_file, scaler=global_scaler, fit_scaler=True)
        # Apply transformation immediately after fitting (for demo simplicity)
        X = global_scaler.transform(X)
        processed_X.append(X)
        processed_y.append(y)
        
    print("\n[+] Preprocessing Pipeline Executed Successfully!")
    print("-" * 50)
    print(f"[>] Example Patient 1 Feature Tensor Shape: {processed_X[0].shape} (Hours, 40 Vitals)")
    print(f"[>] Example Patient 1 Label Tensor Shape:   {processed_y[0].shape} (Hours)")
    
    # Check if Sepsis was flagged in this sample
    total_sepsis_hours = sum([np.sum(labels) for labels in processed_y])
    print(f"[>] Total hours of Sepsis detected in this subset: {total_sepsis_hours}")
    print("-" * 50)
    
    return processed_X, processed_y

if __name__ == "__main__":
    # Point directly to the newly untracked dataset folder
    dataset_path = "/Users/aksharsakhi/Desktop/23CSE399-Project-Phase-1/DetaSets/training_setA"
    
    print("=== FPDAF Phase 2: PhysioNet Preprocessing Engine ===")
    X_data, y_data = build_federated_dataset(dataset_path, max_patients_to_process=200)
    
    print("\n[!] Ready to segment into PyTorch Sliding Windows (LSTM format) and split into Federated Client Nodes!")
