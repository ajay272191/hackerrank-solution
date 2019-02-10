
if __name__ == '__main__':

    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split(' ')))
    for i in range(d):
        
        a.append(a[0])
        a.remove(a[0])
    print(*a)

