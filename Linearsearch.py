
#linear search
n = int(input("Enter the val of n = "))
a = []
for i in range(n):
    ele = int(input("Enter the ele = "))
    a.append(ele)
key = int(input("Enter key = "))
isFound = False
for i in range(n):
    if a[i]==key:
        isFound = True
        print("Key found at pos {}".format(i))

if isFound ==False:
    print(key, " is not found")
