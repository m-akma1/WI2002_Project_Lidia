import pandas as pd
import matplotlib.pyplot as plt

df_sun = pd.read_csv(r"Monday-WorkingHours.pcap_ISCX.csv")
df_wed = pd.read_csv(r"Wednesday-workingHours.pcap_ISCX.csv")

df_sun.columns = df_sun.columns.str.strip()
df_wed.columns = df_wed.columns.str.strip()


labels_v1 = ['SYN Flag Count', 'ACK Flag Count']

mon_v1 = [
    df_sun['SYN Flag Count'].mean(),
    df_sun['ACK Flag Count'].mean()
]

wed_v1 = [
    df_wed['SYN Flag Count'].mean(),
    df_wed['ACK Flag Count'].mean()
]

x1 = range(len(labels_v1))
bar_width = 0.4

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x1], mon_v1, width=bar_width, label='Monday', color='skyblue')
plt.bar([i + bar_width/2 for i in x1], wed_v1, width=bar_width, label='Wednesday', color='salmon')
plt.xticks(x1, labels_v1)
plt.ylabel('Rata-rata Flag Count')
plt.title('SYN vs ACK Flag Count (Monday vs Wednesday)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

labels_v2 = ['Fwd Packet Length Mean', 'Bwd Packet Length Mean']

sun_v2 = [
    df_sun['Fwd Packet Length Mean'].mean(),
    df_sun['Bwd Packet Length Mean'].mean()
]

wed_v2 = [
    df_wed['Fwd Packet Length Mean'].mean(),
    df_wed['Bwd Packet Length Mean'].mean()
]

x2 = range(len(labels_v2))

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x2], sun_v2, width=bar_width, label='Sunday', color='skyblue')
plt.bar([i + bar_width/2 for i in x2], wed_v2, width=bar_width, label='Wednesday', color='salmon')
plt.xticks(x2, labels_v2)
plt.ylabel('Rata-rata Ukuran Paket (bytes)')
plt.title('Fwd vs Bwd Packet Length Mean (Sunday vs Wednesday)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()