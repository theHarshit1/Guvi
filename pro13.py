n,q=list(map(int,input().split()))
l=list(map(int,input().split()))
queries=[]
while(q):
	queries.append(list(map(int,input().split())))
	q-=1
for i in queries:
	print(min(l[i[0]-1:i[1]]))