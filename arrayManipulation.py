
def addd(a,b,k,array,n):

	for i in range(n):
		for j in range(a-1,b):
			array[i][j]+=k
	return(max(max(array)))

if __name__=='__main__':

	s=list(map(int,input().strip().split()))
	n,m=s[0],s[1]
	array=[[0 for i in range(n)] for j in range(n)]
	#print(n,m,"\n",array)
	maxx=0
	for i in range(m):

		s=list(map(int,input().strip().split()))
		a,b,k=s[0],s[1],s[2]
		maxx=addd(a,b,k,array,n)
	print(maxx)
"""5 3
1 2 100
2 5 100
3 4 100
"""