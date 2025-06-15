import pandas as pd

file_monday = r"../data/Monday-filtered.csv"
newfile_monday = r"../data/new_monday.csv"
df_monday = pd.read_csv(file_monday)
df_monday.columns = df_monday.columns.str.strip()

df_monday_clean = df_monday[
    (df_monday['Flow Packets/s'] > 0) &
    (df_monday['Flow Duration'] > 0) &
    (df_monday['Total Backward Packets'] > 0) &
    (df_monday['Flow Bytes/s'] > 0) &
    (df_monday['Average Packet Size'] > 0) &
    (df_monday['Active Mean'] > 0) &
    (df_monday['Idle Mean'] > 0)
]

df_monday_clean.to_csv(newfile_monday, index=False)
print(f"Data Monday bersih disimpan ke: {newfile_monday}")

file_wednesday = r"../data/Wednesday-filtered.csv"
newfile_wednesday = r"../data/new_wednesday.csv"
df_wednesday = pd.read_csv(file_wednesday)
df_wednesday.columns = df_wednesday.columns.str.strip()

df_wednesday_clean = df_wednesday[
    (df_wednesday['Flow Packets/s'] > 0) &
    (df_wednesday['Flow Duration'] > 0) &
    (df_wednesday['Total Backward Packets'] > 0) &
    (df_wednesday['Flow Bytes/s'] > 0) &
    (df_wednesday['Average Packet Size'] > 0) &
    (df_wednesday['Active Mean'] > 0) &
    (df_wednesday['Idle Mean'] > 0)
]

df_wednesday_clean.to_csv(newfile_wednesday, index=False)
print(f"Data Wednesday bersih disimpan ke: {newfile_wednesday}")
