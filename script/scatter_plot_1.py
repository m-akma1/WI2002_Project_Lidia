import pandas as pd
from matplotlib import pyplot as plt

wednesday_file = pd.read_csv('./TrafficLabelling/Wednesday-workingHours.pcap_ISCX.csv', engine='python')

benign = wednesday_file[wednesday_file[' Label'] == 'BENIGN']
attack = wednesday_file[wednesday_file[' Label'] != 'BENIGN']

plt.figure(figsize=(10, 6))
plt.scatter(benign['Bwd Packet Length Max'], benign[' Fwd Packet Length Max'], label='Benign', alpha=0.5, color='blue')
plt.scatter(attack['Bwd Packet Length Max'], attack[' Fwd Packet Length Max'], label='Attack', alpha=0.5, color='red')
plt.xlabel('Bwd Packet Length Max')
plt.ylabel('Fwd Packet Length Max')
plt.title('Bwd Packet Length Max vs Fwd Packet Length Max')
plt.legend()
plt.grid(True)
plt.show()
