import math
n,q=list(map(int,input().split()))
l=list(map(int,input().split()))
queries=[]
while(q):
	queries.append(list(map(int,input().split())))
	q-=1
for i in queries:
	left=i[0]-1
	right=i[1]-1
	if(left==right):
		print(l[left])
		continue
	g=l[left]
	for x in l[left+1:right+1]:
		g=math.gcd(g,x)
	print(g)