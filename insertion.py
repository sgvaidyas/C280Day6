n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)

for i in range(n):
    key = a[i]
    j   = i-1
    while j>=0 and a[j]>key:
        a[j+1] = a[j]
        j-=1
    a[j+1] = key

print("SORTED ELEMENTS ",a)
