n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
s="no"
for i in range(len(l)):
	for j in l[i+1:]:
		if(l[i]+j==k):
			s="yes"
			break
print(s)