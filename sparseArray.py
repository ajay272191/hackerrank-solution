
from collections import Counter

if __name__=='__main__':
    
    s,query=[],[]
    n=int(input())
    for i in range(n):
    	s.append(input())
    q=int(input())
    for i in range(q):
    	query.append(input())
    s=Counter(s)
    print(s.values())
    print(s.keys())
    for x in query:
    	print(s[x])
"""
4
as
asd
as
asdf
3
as
aswe
asdf"""