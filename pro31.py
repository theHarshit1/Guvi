
def maxsum(l):
	for i in l:
		

n,m=map(int,input().split())
g=[]
for _ in range(m):
	a,b=list(map(int,input().split()))
	if a<b:
		g[a].append(b)
	else:
		g[b].append(a)
maxsum(g[0])

