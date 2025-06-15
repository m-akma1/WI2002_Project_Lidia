import pandas as pd
from matplotlib import pyplot as plt

wednesday_file = pd.read_csv('./TrafficLabelling/Wednesday-workingHours.pcap_ISCX.csv', engine='python')

benign = wednesday_file[wednesday_file[' Label'] == 'BENIGN']
attack = wednesday_file[wednesday_file[' Label'] != 'BENIGN']

plt.figure(figsize=(10, 6))
plt.scatter(benign['Idle Mean'], benign['Active Mean'], label='Benign', alpha=0.5, color='blue')
plt.scatter(attack['Idle Mean'], attack['Active Mean'], label='Attack', alpha=0.5, color='red')
plt.xlabel('Idle Mean')
plt.ylabel('Active Mean')
plt.title('Idle Mean vs Active Mean')
plt.legend()
plt.grid(True)
plt.show()
