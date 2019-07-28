def increase(i,prev,c):
	global s
	if(c==3):
		s+=1
		return
	if(i<n): 
		if(l[i]<prev):
			increase(i+1,l[i],c+1)
		increase(i+1,prev,c)
s=0
n=int(input())
l=list(map(int,input().split()))
for i in range(n-2):
	increase(i+1,l[i],1)
print(s)