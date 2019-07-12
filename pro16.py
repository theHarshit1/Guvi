n=int(input())
l=list(map(int,input().split()))
c=[1]*n
for i in range(n-1):
	if(l[i]<l[i+1] and c[i]>=c[i+1]):
		c[i+1]=c[i]+1
for i in range(n-1,0,-1):
	if l[i]<l[i-1] and c[i]>=c[i-1]:
		c[i-1]=c[i]+1
print(*c,sum(c))