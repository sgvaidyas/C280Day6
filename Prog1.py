n = int(input("Enter the val of n = "))
l = ['0'] * (n ** 2)
l[((n - 1) * n)] = '1'


def display():
    for i in range(len(l)):
        if i % n == 0:
            print()
        print(l[i], end="\t")
    print()


def move(direction):
    pos = l.index('1')
    if direction == '8' and pos > n - 1:
        l[pos], l[pos - n] = '0', '1'
    elif direction == '2' and ((n - 1) * n) > pos:
        l[pos], l[pos + n] = '0', '1'
    elif direction == '4' and not pos % n == 0:
        l[pos], l[pos - 1] = '0', '1'
    elif direction == '6' and not pos % n == n-1:
        l[pos], l[pos + 1] = '0', '1'


while True:
    display()
    inp = str(input("Where?"))
    move(inp)
