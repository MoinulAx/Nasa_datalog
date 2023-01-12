from collections import *
import matplotlib.pyplot as plt
import pandas as pd




NASA_file= open("NASA_access_log_Jul95")

plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946' 

colors = [
    '#08F7FE',  
    '#FE53BB',  
    '#F5D300',  
    '#00ff41',  
]

fig, ax = plt.subplots()

IPaddresses=[]
path=[]
type=[]


try:
    for lines in NASA_file:

        # a=lines.split('"')[1]
        # a=a.split('.')[0]
        # a=a.split(' ')[0]
        IPaddresses.append(lines.split(" ")[0])
        # time.append(lines.split(" ")[3])
       
        
        path.append(lines.split(" ")[6])
        # type.append(a)


except UnicodeDecodeError:
    print("uh-oh")


NASA_file.close()
print(f"The most frequent IP was {Counter(IPaddresses).most_common(1)}")

print()


print()

print(f"The most frequent path was {Counter(path).most_common(1)}")

print()

print(f"The most common file type would be {Counter(type).most_common(1)}")

print()

ip_count= Counter(IPaddresses)

# plt.bar(ip_count.keys(),ip_count.values(),align='edge', width=30)



ip_common= Counter(IPaddresses).most_common(10)
ip_values=[]
ip_keys=[]

ax.grid(color='green') 

for i in ip_common:
    ip_keys.append(i[0])
    ip_values.append(i[1])

plt.bar(ip_keys,ip_values,color='green')
plt.xticks(rotation=30)
plt.xlabel('IP Addresses')
plt.ylabel('Amount Searched')


plt.show()



