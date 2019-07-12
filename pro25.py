n=input()
l=list(map(int,input().split()))
max=0
i=0
while(i<len(l)-1):
	c=0
	while(i<len(l)-1 and l[i]<l[i+1]):
		c+=1
		i+=1
	if(c>max):
		max=c
	i+=1
print(max+1)