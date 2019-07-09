n,q=list(map(int,input().split()))
l=list(map(int,input().split()))
queries=[]
while(q):
	queries.append(list(map(int,input().split())))
	q-=1
for i in queries:
	x=0
	for j in range(i[0]-1,i[1]):
		x=x^l[j]
	print(x)