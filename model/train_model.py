import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ----------------------------
# Load and prepare data
# ----------------------------
df = pd.read_csv("data/transactions.csv")

X = df.drop("Class", axis=1).values
y = df["Class"].values

# Stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32)

# ----------------------------
# Define model
# ----------------------------
class FraudNet(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

model = FraudNet(X_train.shape[1])

# ----------------------------
# Handle class imbalance
# ----------------------------
fraud_weight = (len(y_train) - y_train.sum()) / y_train.sum()
criterion = nn.BCELoss(weight=torch.tensor(fraud_weight))
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# ----------------------------
# Training loop
# ----------------------------
epochs = 5
for epoch in range(epochs):
    model.train()
    preds = model(X_train).squeeze()
    loss = criterion(preds, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

# ----------------------------
# Save model
# ----------------------------
torch.save(model.state_dict(), "model/fraud_model.pt")
print("Model saved to model/fraud_model.pt")
