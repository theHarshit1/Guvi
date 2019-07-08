x,y=input().strip().split(" ")
c=0
for a ,b in zip(x,y):
	if(a==b):
		c+=1
cost=0
if(len(x)>len(y)):
	cost=len(x)-c
else:
	cost=len(y)-c
print(cost)