from collections import *
import matplotlib.pyplot as plt
import pandas as pd




NASA_file= open("NASA_access_log_Jul95")

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


for i in ip_common:
    ip_keys.append(i[0])
    ip_values.append(i[1])

plt.bar(ip_keys,ip_values,color='red')
plt.xticks(rotation=30)


plt.show()



