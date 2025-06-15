import pandas as pd

# Load dataset
df = pd.read_csv("../data/new_wednesday.csv")

# Essential columns you want
essential_columns = [
    'Source IP', 'Source Port', 'Protocol', 'Timestamp',
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Flow Bytes/s', 'Flow Packets/s', 'Fwd Packet Length Mean',
    'Bwd Packet Length Mean', 'SYN Flag Count', 'ACK Flag Count',
    'Down/Up Ratio', 'Average Packet Size', 'Active Mean', 'Idle Mean',
    'Label'
]

# Filter to only essential columns
df = df[essential_columns]

# Convert necessary columns to numeric (if needed)
numeric_cols = [
    'Source Port', 'Protocol', 'Flow Duration', 'Total Fwd Packets',
    'Total Backward Packets', 'Flow Bytes/s', 'Flow Packets/s',
    'Fwd Packet Length Mean', 'Bwd Packet Length Mean',
    'SYN Flag Count', 'ACK Flag Count', 'Down/Up Ratio',
    'Average Packet Size', 'Active Mean', 'Idle Mean'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # convert and handle errors

# Drop non-numeric columns and keep only numerics
df_numeric = df[numeric_cols]

# Drop rows with NaN values in numeric fields (optional)
df_numeric_clean = df_numeric.dropna()

# Compute standard descriptive statistics
desc = df_numeric_clean.describe().T  # .T to transpose for better readability

# Compute additional percentiles
desc['10%'] = df_numeric_clean.quantile(0.10)
desc['90%'] = df_numeric_clean.quantile(0.90)

# Reorder columns if desired
desc = desc[['count', 'mean', 'std', '10%', '25%', '50%', '75%', '90%', 'max', 'min']]

# Display
# Reorder columns if desired
desc = desc[['count', 'mean', 'std', '10%', '25%', '50%', '75%', '90%', 'max', 'min']]

# Output to a CSV file
desc.to_csv("../data/Wednesday-statdes.csv", index=True)  # index=True to include row labels (feature names)

