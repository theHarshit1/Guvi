n=int(input())
l=list(map(int,input().split()))
j=1
for i in range(len(l)):
	if l[i] in l[i+1:]:
		while(j in l):
			j+=1
		l[i]=j
print(j)
print(*l,sep=' ')