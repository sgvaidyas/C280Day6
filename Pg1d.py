n = int(input("Enter the n = "))
ind = bottomCorner = n**2 - n
l = [0]*(n**2)
l[bottomCorner]= 1
def display():
    for i in range(n**2):
        if i%n==0:
            print()
        print(l[i],end="\t")
    print()
display()
while True:
    print(" UP 8 \n DOWN 2 \n LEFT 4\n RIGHT 6")
    ch = int(input("Enter choice = "))
    invalid = False
    pos = 0
    if ch==8:
        if ind-n<0:
            msg = "Cannot move UP .. Time to buy specs"
            invalid = True
        else:
            pos = -n
    elif ch==2:
        if ind+n>=n*n:
           msg = "Cannot move DOWN .. Time to buy specs"
           invalid = True
        else:
            pos = n
    elif ch==4:
        if ind%n==0:
           msg = "Cannot move LEFT .. Time to buy specs"
           invalid = True
        else:
            pos = -1
    elif ch==6:
        if ind%n==n-1:
            msg = "Cannot move RIGHT .. Time to buy specs"
            invalid = True
        else:
            pos=1
    if not invalid:
        l[ind]=0
        l[ind+pos]=1
        ind=ind+pos
    else:
        print(msg)
    display()
