n,m=map(int,input().split())
l=[]
for _ in range(n):
	l.append(input())
sum=0
for i in l:
	a=b=0
	for j in range(0,m-1,2):
		if(i[j]=='R'):
			a+=5
		if(i[j+1]=='G'):
			a+=3
		if(i[j]=='G'):
			b+=3
		if(i[j+1]=='R'):
			b+=5
	sum+=min(a,b)
print(sum)