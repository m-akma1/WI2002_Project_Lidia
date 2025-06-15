import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Configuration ===
input_csv = '../data/Wednesday-cleaned.csv'
output_folder = '../output'
output_file = 'correlation_heatmap_wed_clean.png'

# === Load Dataset ===
df = pd.read_csv(input_csv, low_memory=False)

# === Select Only Quantitative Attributes ===
# Exclude non-numeric columns like 'Source IP', 'Protocol', 'Label', 'Timestamp'
non_numeric_cols = ['Source IP', 'Protocol', 'Label', 'Timestamp']
quantitative_cols = [col for col in df.columns if col not in non_numeric_cols]

# Keep only numeric columns
quantitative_df = df[quantitative_cols].select_dtypes(include=['number'])

# === Compute Correlation Matrix ===
corr = quantitative_df.corr()

# === Plot Correlation Heatmap ===
plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap of Quantitative Attributes')

# === Ensure output directory exists ===
os.makedirs(output_folder, exist_ok=True)

# === Save Figure ===
plt.tight_layout()
plt.savefig(os.path.join(output_folder, output_file), dpi=300)
plt.close()

print(f"[INFO] Correlation heatmap saved to '{os.path.join(output_folder, output_file)}'")
