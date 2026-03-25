import torch
import torch.nn as nn
import torch.nn.functional as F

class TemporalAttention(nn.Module):
    """
    Computes attention weights over the time steps of the LSTM output.
    Provides explainability by highlighting the most relevant historical timestamps.
    """
    def __init__(self, hidden_dim):
        super(TemporalAttention, self).__init__()
        self.attention = nn.Linear(hidden_dim, 1, bias=False)

    def forward(self, lstm_output):
        # lstm_output shape: (batch_size, seq_len, hidden_dim)
        attn_scores = self.attention(lstm_output) # (batch_size, seq_len, 1)
        attn_weights = F.softmax(attn_scores, dim=1) # (batch_size, seq_len, 1)
        
        # Context vector
        context_vector = torch.sum(attn_weights * lstm_output, dim=1) # (batch_size, hidden_dim)
        
        return context_vector, attn_weights

class LocalPersonalizedModel(nn.Module):
    """
    FPDAF Architecture Element: 
    A shared global LSTM backbone paired with an Attention layer and a Local Personalization Head.
    """
    def __init__(self, input_dim, hidden_dim, output_dim, num_layers=2):
        super(LocalPersonalizedModel, self).__init__()
        
        # 1. Global Shared Backbone (LSTM)
        self.lstm = nn.LSTM(input_size=input_dim, 
                            hidden_size=hidden_dim, 
                            num_layers=num_layers, 
                            batch_first=True)
        
        # 2. Explainable Attention Layer
        self.attention = TemporalAttention(hidden_dim)
        
        # 3. Local Personalization Head (Not shared during Federated Aggregation)
        self.personalization_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, output_dim)
        )

    def forward(self, x):
        # x shape: (batch_size, seq_len, num_features)
        lstm_out, _ = self.lstm(x)
        
        # Apply attention
        context_vector, attn_weights = self.attention(lstm_out)
        
        # Pass through local personalization head
        predictions = self.personalization_head(context_vector)
        
        return predictions, attn_weights

    def get_global_parameters(self):
        """Returns parameters that should be uploaded to the Aggregator."""
        return list(self.lstm.parameters()) + list(self.attention.parameters())
    
    def get_local_parameters(self):
        """Returns parameters that remain strictly local (for handling non-IID data & drift)."""
        return list(self.personalization_head.parameters())

if __name__ == "__main__":
    # Test the model structure
    batch_size = 16
    seq_len = 24  # e.g., 24 hours of patient history
    features = 3  # e.g., HR, BP, SpO2
    
    dummy_vitals = torch.rand(batch_size, seq_len, features)
    model = LocalPersonalizedModel(input_dim=features, hidden_dim=64, output_dim=1)
    
    preds, weights = model(dummy_vitals)
    print("Testing Architecture Implementation...")
    print(f"Prediction shape (Risk Score): {preds.shape}")
    print(f"Attention weights shape (Explainability): {weights.shape}")
