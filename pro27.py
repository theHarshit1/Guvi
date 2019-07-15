n,w=map(int,input().split())
weights=list(map(int,input().split()))
val=list(map(int,input().split()))
r=[]
for i in range(n):
	if(weights[i]>w):
		del weights[i]
		del val[i]
n=len(val)
for i in range(n):
	r.append(val[i]/weights[i])
sum=0
tot=0
l=sorted(zip(r,val,weights),reverse=True)
for _,x,y in l:
	if(sum+y<=w):
		sum+=y
		tot+=x
print(tot)
