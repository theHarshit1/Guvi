n,m=map(int,input().split())
l=[]
for _ in range(n):
	l.append(list(map(int,input().split())))
for i in range(len(l)):
	if(0 in l[i]):
		l[i]=l[i].remove(0)
lengths=[]
for i in l:
	lengths.append(len(l))
max=0
for i in lengths[::-1]:
	if(i==lengths.count(i)):
		max=i
		break
s=((str(1)+" ")*max).strip()
#for i in range(max):
#	print(s)
print(*l)
