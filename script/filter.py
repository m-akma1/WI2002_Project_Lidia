import pandas as pd

# === Configuration ===
input_csv = '../data/Monday-WorkingHours.pcap_ISCX.csv'  # Replace with your actual file path
output_csv = '../data/Monday-filtered.csv'

# === Attributes to Keep ===
selected_columns = [
    'Source IP',
    'Source Port',
    'Protocol',
    'Timestamp',
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Flow Packets/s',
    'Fwd Packet Length Mean',
    'Bwd Packet Length Mean',
    'SYN Flag Count',
    'ACK Flag Count',
    'Down/Up Ratio',
    'Average Packet Size',
    'Active Mean',
    'Idle Mean',
    'Label'
]

# === Load and Filter Dataset ===
df = pd.read_csv(input_csv, low_memory=False)

# Ensure all selected columns exist in the file
missing = [col for col in selected_columns if col not in df.columns]
if missing:
    print(f"[ERROR] Missing columns: {missing}")
else:
    filtered_df = df[selected_columns]
    filtered_df.to_csv(output_csv, index=False)
    print(f"[INFO] Filtered data saved to '{output_csv}'")
