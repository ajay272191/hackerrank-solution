
if __name__=='__main__':

    n=int(input())
    s=input().strip().split()
    result=[]
    for i in range(n):

        result.append(s[n-1-i])
    print(*result)