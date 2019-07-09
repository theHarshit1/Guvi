n=int(input())
l=list(map(int,input().split()))
i=1
sum=0
while(i<n):
	for x in l[:i]:
		if(x<l[i]):
			sum+=x
	i+=1
print(sum)