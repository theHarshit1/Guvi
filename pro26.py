c=[]
def sub(a,prev,count):
	if(a[0]>prev):
		count+=1
		c.append(count)
		if(len(a)>1):
			sub(a[1:],a[0],count)
	if(len(a)>1):
		sub(a[1:],a[1],1)
n=input()
l=list(map(int,input().split()))
sub(l,0,1)
print(c)
