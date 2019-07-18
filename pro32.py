n,m=map(int,input().split())
l=[]
for _ in range(n):
	l.append(sorted(list(map(int,input().split()))))
for i in range(n-1):
	for j in range(m):
		for k in range(n-i):
			if(l[i][j]>l[i+k][j]):
				l[i][j],l[i+k][j]=l[i+k][j],l[i][j]
for i in l:
	print(*i,sep=' ')
