import pandas as pd
import matplotlib.pyplot as plt


file_path = '../data/new_wednesday.csv'
data = pd.read_csv(file_path)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce', dayfirst=True)
data = data.dropna(subset=['Timestamp'])
filtered_data = data
features_to_plot = [
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
    'Idle Mean'
]

filtered_data = filtered_data.replace([float('inf'), -float('inf')], pd.NA)
filtered_data = filtered_data.dropna(subset=features_to_plot)

i = 1
for i in range(13):
    feature = features_to_plot[i]
    fig, ax = plt.subplots(figsize=(14, 5))
    
    ax.plot(filtered_data['Timestamp'], filtered_data[feature], label=feature, color='tab:blue', linewidth=0.8)
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(feature)
    ax.set_title(f'{feature} Over Time')
    ax.grid(True)
    ax.legend()
    plt.xticks(rotation=45)
    fig.tight_layout()
    
    fig.savefig(f'../output/plot_{feature.replace(" ", "_").replace("/", "_").replace("\\", "_")}.png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    i += 1
