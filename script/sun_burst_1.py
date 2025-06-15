import matplotlib.pyplot as plt
import numpy as np
import pandas
 
import plotly.express as px
 
data = pandas.read_csv(r"Wednesday.csv")      
 
FD = data[' Flow Duration'].tolist()
TFwdP = data[' Total Fwd Packets'].tolist()
TBwdP = data[' Total Backward Packets'].tolist()
L = data[' Label'].tolist()
 
LReasoning = []
LActivity = []
LCategorized = []
LParent = []
LAmount = []
LWhole = []
 
 
 
for x in L :
    found = False
    for y in range(len(LCategorized)) :
        if x == LCategorized[y] :
            found = True
    
    if found == False :
        LCategorized.append(x)
        LCategorized.append(x)
        LCategorized.append(x)
        LCategorized.append(x)
        LActivity.append("Normal Activity")
        LActivity.append("Abnormal Activity")
        LActivity.append("Abnormal Activity")
        LActivity.append("Abnormal Activity")
        LReasoning.append(None)
        LReasoning.append("Flow Duration too High")
        LReasoning.append("No Flow Duration")
        LReasoning.append("Abnormal Packet Volume")
        LAmount.append(0)
        LAmount.append(0)
        LAmount.append(0)
        LAmount.append(0)
 
for i in range(len(FD)) :
    y = L[i]
    if ((TFwdP[i] <= 7) and (TBwdP[i] <= 6) and (FD[i] <= 889097) and (FD[i] > 0)) :
        x = "Normal Activity"
        z = None
    else :
        x = "Abnormal Activity"
        if (FD[i] <= 0) :
            z = "No Flow Duration"
        elif (FD[i] > 889097):
            z = "Flow Duration too High"
        else :
            z = "Abnormal Packet Volume"
 
    for j in range(len(LCategorized)) :
        if (LCategorized[j] == y) and (LActivity[j] == x) and (LReasoning[j] == z):
            LAmount[j] += 1
 
 
for x in LCategorized :
    if (x == "BENIGN") :
        LParent.append("")
    else :
        LParent.append("HOSTILE")
 
for x in LParent :
    LWhole.append("Traffic Activity")
 
 
sun_data = dict(E=np.array(LReasoning), C=np.array(LActivity), A = np.array(LCategorized), B = np.array(LParent), D = np.array(LWhole), value = np.array(LAmount))
 
fig = px.sunburst(
    sun_data,
    path = ['D', 'B', 'A', 'C', 'E'],
    values = 'value',
    height= 1000, width=1000,
    title="Hierarki Aktivitas Lalu Lintas di Hari Rabu 5 Juli 2017 Berdasarkan Penyebab Gangguan Lalu Lintas")
 
fig.show()