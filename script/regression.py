import pandas as pd
import numpy as np
from sklearn.linear_model import linearregression
import matplotlib.pyplot as plt

file_monday = r"wednesday-workinghours.pcap_iscx.csv"
df = pd.read_csv(file_monday)
df.columns = df.columns.str.strip()
x = df[['total fwd packets', 'flow duration']]
y = df['flow bytes/s']
model = linearregression()
model.fit(x, y)
plt.figure(figsize=(8,5))
plt.scatter(x['total fwd packets'], y, color='blue', alpha=0.5, label='data sebenarnya')

# prediksi untuk membuat garis regresi
x_line = np.linspace(x['total fwd packets'].min(), x['total fwd packets'].max(), 100)
x_pred = pd.dataframe({'total fwd packets': x_line, 'flow duration': np.mean(x['flow duration'])})
y_pred = model.predict(x_pred)

plt.plot(x_line, y_pred, color='red', label='garis regresi')
plt.xlabel('total fwd packets')
plt.ylabel('flow bytes/s')
plt.title('regresi linear: total fwd packets vs flow bytes/s (monday)')
plt.legend()
plt.grid(true)
plt.show()
