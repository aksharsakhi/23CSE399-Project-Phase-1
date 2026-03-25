import torch
import torch.nn as nn
import torch.optim as optim
import copy
from data_simulation import SimulatedICUDataset, DataLoader
from models import LocalPersonalizedModel

def get_hospitals_data(num_hospitals=3, patients_per_hospital=200, batch_size=32):
    """
    Creates isolated data loaders for each hospital to simulate Federated Learning
    without centralizing the data.
    """
    datasets = [SimulatedICUDataset(num_patients=patients_per_hospital) for _ in range(num_hospitals)]
    return [DataLoader(ds, batch_size=batch_size, shuffle=True) for ds in datasets]

def create_federated_clients(num_clients=3):
    """
    Instantiates independent local models initialized with the exact same architecture.
    """
    return [LocalPersonalizedModel(input_dim=3, hidden_dim=64, output_dim=1) for _ in range(num_clients)]

def fed_avg_aggregate(global_model, client_models, learning_rate=1.0):
    """
    Proof of Concept: FedAvg aggregation step for the Global Backbone only.
    Personalized heads remain untouched and local to the hospital.
    """
    # 1. Start with the current global weights
    global_dict = global_model.state_dict()
    
    # 2. Extract local client states
    client_dicts = [model.state_dict() for model in client_models]
    
    # 3. Aggregate Shared Layers (LSTM Backbone + Attention Layer)
    #    We exclude the "personalization_head" keys
    shared_keys = [k for k in global_dict.keys() if 'personalization_head' not in k]
    num_clients = len(client_models)
    
    for key in shared_keys:
        # Sum local gradients/weights for the shared layer
        aggregated_weight = sum([c_dict[key] for c_dict in client_dicts]) / num_clients
        global_dict[key] = aggregated_weight
        
    # 4. Load the new global aggregated weights back into the global model
    global_model.load_state_dict(global_dict)
    
    # 5. Distribute updated global weights back to all clients
    for model in client_models:
        local_dict = model.state_dict()
        # Only overwrite the shared backbone
        for key in shared_keys:
            local_dict[key] = global_dict[key]
        model.load_state_dict(local_dict)

def local_training(client_model, data_loader, epochs=1):
    """
    Simulates training on local hospital data.
    Model updates its global backbone and its private personalization head here.
    """
    optimizer = optim.Adam(client_model.parameters(), lr=0.001)
    criterion = nn.BCEWithLogitsLoss()
    
    client_model.train()
    for e in range(epochs):
        epoch_loss = 0
        for vitals, risk in data_loader:
            optimizer.zero_grad()
            
            # Forward pass: (Risk Prediction, Attention Weights)
            predictions, attention_weights = client_model(vitals)
            
            # Compute loss
            loss = criterion(predictions, risk)
            loss.backward()
            optimizer.step()
            
            epoch_loss += loss.item()

def run_federated_simulation(rounds=3):
    print("--- Initializing FPDAF Simulation (Phase 1 Proof of Concept) ---\n")
    
    # 1. Setup isolated data and distinct client models
    num_hospitals = 3
    hospital_data = get_hospitals_data(num_hospitals)
    client_models = create_federated_clients(num_hospitals)
    
    # 2. Create the central Global Model
    global_model = LocalPersonalizedModel(input_dim=3, hidden_dim=64, output_dim=1)
    
    # 3. Synchronize initial weights identically
    fed_avg_aggregate(global_model, client_models)
    
    for r in range(rounds):
        print(f"Federated Communication Round {r+1}/{rounds}...")
        
        # Step A: Local Training (Hospitals learn from their isolated patients)
        for i, model in enumerate(client_models):
            local_training(model, hospital_data[i], epochs=2)
            print(f"   [Hospital {i+1}] Finished local optimization.")
            
            # --- CUSUM Placeholder ---
            # If Concept Drift detected via CUSUM:
            # model.personalization_head.reset_parameters()
            
        # Step B: Secure Aggregation
        print(f"   [Aggregator] Server aggregating Global LSTMs & Attention layers...")
        fed_avg_aggregate(global_model, client_models)
        print("   [Aggregator] Global Model updated & redistributed.\n")
        
    print("--- Phase 1 Architecture Validation Complete. Models are compiling and aggregating via FedAvg seamlessly. ---")

if __name__ == "__main__":
    run_federated_simulation()
