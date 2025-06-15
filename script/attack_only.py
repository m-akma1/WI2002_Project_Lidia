import pandas as pd

input_csv = '../data/Wednesday-filtered.csv'
output_csv = '../data/Wednesday-attacks-only.csv'

df = pd.read_csv(input_csv, low_memory=False)


attacks_df = df[df['Label'] != 'BENIGN']


attacks_df.to_csv(output_csv, index=False)
print(f"[INFO] Non-BENIGN (attack-only) data saved to '{output_csv}'")
