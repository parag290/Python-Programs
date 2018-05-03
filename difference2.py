
lists = [
    [1,2,3],
    [4,5,2,9],
    [2,6,7]
]


i = 0
n = len(lists)-1
l1 = []

while(i < n):
    l1.append([x-y for x,y in zip(lists[i],lists[i+1])])
    i += 1
print(l1)



i = 0
l2 = []
while(i<n):
    l2.append(list((set(lists[i]) | set(lists[i+1])) - (set(lists[i]) & set(lists[i+1]))))
    i += 1
print(l2)
