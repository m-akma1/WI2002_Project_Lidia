import matplotlib.pyplot as plt import numpy as np import pandas
import plotly.express as px
data = pandas.read_csv(r"Wednesday.csv") 

Timestamp = data[' Timestamp'].tolist() 
L = data[' Label'].tolist()

def getHour(time) : 
    time = time[9:] 
    hour = "" 
    for x in time : 
        if (x == ':') : 
            ihour = int(hour) 
            if ihour < 8 : 
                hour += " PM" 
            else : 
                hour += " AM"
            iihour = ihour + 1
            if iihour > 12 :
                iihour -= 12
            hour += " - " + str(iihour)
            if iihour < 8 :
                hour += " PM"
            else :
                hour += " AM"
            return hour
    
        hour += x
 
LReasoning = [] 
LActivity = [] 
LCategorized = [] 
LTimed = [] 
LParent = [] 
LAmount = [] 
LWhole = []
for x in Timestamp : 
    found = False 
    for y in range(len(LTimed)) : 
        if getHour(x) == LTimed[y] : 
            found = True
    if found == False :
        LTimed.append(getHour(x))
    
    
 
LTimed_ = []
for x in L : 
    found = False 
    for y in range(len(LCategorized)) : 
        if x == LCategorized[y] : 
            found = True
    if found == False :
        for w in LTimed :
            LTimed_.append(w)
            LCategorized.append(x)
            LAmount.append(0)
 
LCategorized_ = []
for i in range(len(L)) : 
    y = L[i] 
    x = getHour(Timestamp[i])
    for j in range(len(LCategorized)) :
        if (y == LCategorized[j]) and (x == LTimed_[j]) :
            LAmount[j] += 1
 
for x in LCategorized : 
    if (x == "BENIGN") : 
        LParent.append("BENIGN") 
    else : 
        LParent.append("HOSTILE")

for x in LCategorized : 
    if (x == "BENIGN") : 
        LCategorized_.append(None) 
    else : 
        LCategorized_.append(x)

for x in LParent : 
    LWhole.append("Traffic Activities from 8AM - 6PM")

sun_data = dict(A = np.array(LCategorized_),B = np.array(LParent), C=np.array(LTimed_), D = np.array(LWhole), value = np.array(LAmount))

fig = px.sunburst( sun_data, path = ['D', 'C', 'B', 'A'], values = 'value', height= 1000, width=1000, title="Hierarki Aktivitas Lalu Lintas di Hari Rabu 5 Juli 2017 Berdasarkan Keakitfan Serangan pada Selang Waktu")
fig.show()
