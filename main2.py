from collections import *
import matplotlib.pyplot as plt
import pandas as pd



NASA_file= open("NASA_access_log_Jul95")


plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  

times=[]

colors = [
    '#08F7FE',  
    '#FE53BB',  
    '#F5D300',  
    '#00ff41',  
]

try:
    for lines in NASA_file:
        time=lines.split(' ')[3]
        time=time.split(':')[0]
        time=time.split('[')[1]
        time=time.split('/1995')[0]
        times.append(time)
except UnicodeDecodeError:
    print('uh-oh')




time_common= Counter(times).most_common(10)
timekeys = Counter(times).keys()
timevalues = Counter(times).values()
print(timekeys)
print(timevalues)
time_value=[]
time_key=[]

fig, ax = plt.subplots()

for z in time_common:
    time_key.append(z[0])
    time_value.append(z[1])



plt.plot(timekeys,timevalues,
    color='#08F7FE',
    marker="o",
    )

plt.xticks(rotation=30)

ax.grid(color='#2A3459') 

plt.xlabel("DATES")
plt.ylabel("Amount of Searches")

plt.show()


print(f"The most frequent date was {Counter(time).most_common(1)}")
