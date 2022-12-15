from collections import *
NASA_file= open("NASA_access_log_Jul95")

IPaddresses=[]
time=[]
path=[]
type=[]


try:
    for lines in NASA_file:

        a=lines.split('"')[1]
        a=a.split('.')[1]
        a=a.split(' ')[0]
        IPaddresses.append(lines.split(" ")[0])
        time.append(lines.split(":")[0])
        path.append(lines.split(" ")[6])
        type.append(a)


except:
    print("uh-oh")


print(f"The most frequent IP was {Counter(IPaddresses).most_common(1)}")

print()

print(f"The most frequent date was {Counter(time).most_common(1)}")

print()

print(f"The most frequent path was {Counter(path).most_common(1)}")

print()

print(f"The most common file type would be {Counter(type).most_common(1)}")
