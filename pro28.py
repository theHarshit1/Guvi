n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
sum=0
c=0
for i in l:
	if(sum<=i):
		c+=1
	sum+=i
print(c)