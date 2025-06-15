import pandas as pd
import numpy as np

input_csv = '../data/Monday-filtered.csv'
output_csv = '../data/Monday-cleaned.csv'

df = pd.read_csv(input_csv, low_memory=False)

numeric_cols = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Flow Packets/s',
    'Fwd Packet Length Mean',
    'Bwd Packet Length Mean',
    'Average Packet Size',
    'Active Mean',
    'Idle Mean',
    'SYN Flag Count',
    'ACK Flag Count',
    'Down/Up Ratio',
    'Source Port'  # Port numbers >= 0
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=numeric_cols)

for col in numeric_cols:
    df = df[df[col] >= 0]

df['Label'] = df['Label'].str.strip().str.upper()

df = df[df['Label'] != '']

df.to_csv(output_csv, index=False)
print(f"[INFO] Cleaned dataset saved to '{output_csv}'")
