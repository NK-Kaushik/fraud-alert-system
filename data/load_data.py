import pandas as pd

# Load dataset
df = pd.read_csv("data/transactions.csv")

# Basic inspection
print("Shape:", df.shape)
print(df.head())

# Class distribution
print("\nClass distribution:")
print(df["Class"].value_counts())

# Fraud percentage
fraud_ratio = df["Class"].mean()
print(f"\nFraud rate: {fraud_ratio:.4f}")
