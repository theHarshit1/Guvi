n=int(input())
p=2**n
l=[]
for i in range(n):
	l.append([])
for j in range(1,p):
	s=format(j,'0'+str(n)+'b')
	l[s.count('1')-1].append(s)
print('0'*n)
for i in l:
	print(*i,sep='\n')