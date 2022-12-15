from collections import *
NASA_file= open("NASA_access_log_Jul95")

IPaddresses=[]


try:
    for lines in NASA_file:
        
        IPaddresses.append(lines.split(" ")[0])
        


except:
    print("uh-oh")


print(Counter(IPaddresses))
