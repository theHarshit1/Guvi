n=input()
l=list(map(int,input().split()))
max=0
for i in range(len(l)):
	c=0
	prev=l[i]
	for j in range(i+1,len(l)):
		if(l[j]>prev):
			c+=1
			prev=l[j]
	if(c>max):
		max=c
print(max)