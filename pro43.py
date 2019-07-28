n=int(input())
l=list(map(int,input().split()))
ntimes=[]
visited=[]
c=0
for i in range(n):
	ntimes.append(l.count(i+1))
for i in range(n):
	if(ntimes[l[i]-1]>1):
		ind=ntimes.index(0)+1
		if(l[i]>ind or l[i] in visited):
			ntimes[l[i]-1]-=1
			l[i]=ind
			ntimes[l[i]-1]=1
			c+=1
		else:
			visited.append(l[i])
print(c)
print(*l)