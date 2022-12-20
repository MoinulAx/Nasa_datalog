from collections import *
import matplotlib.pyplot as plt



fruits=[
'banana',
'apple','apple',
'oranges','oranges','oranges',
'cherry','cherry','cherry','cherry'
]

fruits_counter= Counter(fruits)

print(fruits_counter)

print(fruits_counter.keys())
print(fruits_counter.values())

plt.bar(fruits_counter.keys(),fruits_counter.values())


plt.show()

# dct={'cherry': 4, 'oranges': 3, 'apple': 2, 'banana': 1}

# print(dct['apple'])