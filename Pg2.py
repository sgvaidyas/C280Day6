a = [11,2,44,2,4,5,2,6,7,8]
occurances = a.count(2)
i=0
newind=0
while i<occurances:
    newind = a.index(2,newind)
    print(newind)
    newind+=1
    i+=1


