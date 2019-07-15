x,y=input().split()
if len(x)>len(y):
	n=len(y)
else:
	n=len(x)
cost=0
for i in range(n):
	if x[i]!=y[i]:
		cost+=abs(ord(x[i])-ord(y[i]))
z=x[n:]+y[n:]
for i in z:
	cost+=ord(i)-96
print(cost)
