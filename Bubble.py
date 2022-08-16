n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)

#bubble sort
for i in range(n-1):
    for j in range(n-1-i):
        if a[j]<a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a)
