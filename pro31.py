def maxsum(l,count):
	if(len(l)==0):
		return count
	x=maxsum(g[l[0]-1],count+l[0])
	y=maxsum(l[1:],count)
	return max(x,y)

n,m=map(int,input().split())
g=[]
for _ in range(n):
	g.append([])
for _ in range(m):
	a,b=list(map(int,input().split()))
	g[a-1].append(b)
s=maxsum(g[0],1)
print(s)
