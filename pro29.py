n=int(input())
l=[]
for i in range(n):
	r=0
	d=i
	while(d>0):
		r+=(d%10)
		d=d//10
	if(r+i==n):
		l.append(i)
print(len(l),*l,sep='\n')