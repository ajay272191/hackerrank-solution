
if __name__ == '__main__':
	
	t=int(input())
	for x in range(t):

		s=input().strip()
		even,odd=[],[]
		for i in range(len(s)):

			if(i%2==0):
				even.append(s[i])
			else:
				odd.append(s[i])
		print("".join(even),"".join(odd))