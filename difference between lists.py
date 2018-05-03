from collections import Counter
from itertools import chain


list_of_lists = [
    [1,2,3],
    [4,5,2],
    [2,6,7]
]

print("Given List is : ")
print(list_of_lists)
print("\n")

n = len(list_of_lists)

counts = Counter(chain.from_iterable(list_of_lists))
#print(counts)
unique_list = [k for k, c in counts.items() if c == 1]

print("unique numbers are : ")
print(unique_list)
print("\n")
print("Common numbers are : ")
print([k for k, c in counts.items() if c == n])
