k=int(input())
l=[]
while(k):
	l+=list(map(int,input().split()))
	k-=1
l=sorted(l)
print(*l)