import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np

class SimulatedICUDataset(Dataset):
    """
    Simulates high-frequency ICU Data representing the core architecture gap:
    Features: Heart Rate, Blood Pressure, SpO2.
    Labels: Risk score for severe physiological decline over the next hour.
    """
    def __init__(self, num_patients, seq_len=24, features=3):
        # Generate dummy but structured multivariate time-series data
        self.num_patients = num_patients
        self.seq_len = seq_len
        self.features = features
        
        # Simulating baselines for each feature (e.g., HR=70, BP=120, SpO2=98)
        self.baselines = np.array([70.0, 120.0, 98.0])
        
        # 1. Generate normal vitals
        self.data = np.random.normal(loc=self.baselines, scale=[10, 15, 2], 
                                     size=(num_patients, seq_len, features))
        
        # 2. Add realistic variance simulating hospital demographics (Heterogeneity)
        demographic_shift = np.random.uniform(-5, 5, size=(num_patients, 1, features))
        self.data += demographic_shift
        
        # 3. Simulate target risk (Simple heuristic based on specific abnormal vitals)
        # e.g., low BP + high HR often predicts risk
        self.targets = []
        for p in range(num_patients):
            last_hr = self.data[p, -1, 0]
            last_bp = self.data[p, -1, 1]
            last_spo2 = self.data[p, -1, 2]
            
            # Risk logic: Tachycardia OR Hypotension
            if (last_hr > 100) or (last_bp < 90) or (last_spo2 < 92):
                risk = 1.0 # High risk
            else:
                risk = 0.0 # Low risk
            self.targets.append([risk])
            
        self.targets = np.array(self.targets)

        # Convert to Tensors
        self.data = torch.FloatTensor(self.data)
        self.targets = torch.FloatTensor(self.targets)

    def __len__(self):
        return self.num_patients

    def __getitem__(self, idx):
        return self.data[idx], self.targets[idx]

def get_hospital_data(hospital_size=100, batch_size=16):
    """Returns a PyTorch DataLoader for a specific Hospital node."""
    dataset = SimulatedICUDataset(num_patients=hospital_size)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)

if __name__ == "__main__":
    print("Testing ICU Data Simulation (Phase 1 Stub)...")
    loader = get_hospital_data(hospital_size=50)
    for X, y in loader:
        print(f"Batch Structure -> Vitals: {X.shape}, Targets: {y.shape}")
        print(f"Sample First Vitlas: {X[0][0]}")
        break
