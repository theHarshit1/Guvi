n,q=list(map(int,input().split()))
l=list(map(int,input().split()))
queries=[]
while(q):
	queries.append(list(map(int,input().split())))
	q-=1
for x in queries:
	print(sum(l[x[0]-1:x[1]]))