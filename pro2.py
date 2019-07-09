n,k=input().strip().split(" ")
k=int(k)
i=0;
size=len(n)
while i<size-1 and k:
	if(n[i]>n[i+1]):
		k-=1
		n=n.replace(n[i],"")
		if(i!=0):
			i-=1
	else:
		i+=1
res=n[:len(n)-k]
print(res)