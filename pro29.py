n=int(input())
l=[]
m=len(str(n))
s=0
for _ in range(m):
	s+=9
for i in range(n-s,n):
	r=0
	d=i
	while(d>0):
		r+=(d%10)
		d=d//10
	if(r+i==n):
		l.append(i)
print(len(l),*l,sep='\n')