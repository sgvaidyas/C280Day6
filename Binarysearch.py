#linear search
n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)
key = int(input("Enter key = "))

low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if a[mid]==key:
        print(key , " found at pos = ",mid)
        break
    elif a[mid]<key:
        low = mid+1
    else:
        high=mid-1
if low>high:
    print(key, "not found ")
