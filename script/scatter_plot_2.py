import pandas as pd
from matplotlib import pyplot as plt

wednesday_file = pd.read_csv('./TrafficLabelling/Wednesday-workingHours.pcap_ISCX.csv', engine='python')

benign = wednesday_file[wednesday_file[' Label'] == 'BENIGN']
attack = wednesday_file[wednesday_file[' Label'] != 'BENIGN']

plt.figure(figsize=(10, 6))
plt.scatter(benign[' Fwd IAT Mean'], benign[' Bwd IAT Mean'], label='Benign', alpha=0.5, color='blue')
plt.scatter(attack[' Fwd IAT Mean'], attack[' Bwd IAT Mean'], label='Attack', alpha=0.5, color='red')
plt.xlabel('Fwd IAT Mean')
plt.ylabel('Bwd IAT Mean')
plt.title('Fwd IAT Mean vs Bwd IAT Mean')
plt.legend()
plt.grid(True)
plt.show()
