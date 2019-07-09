x,y=input().strip().split(" ")
count=0
for a ,b in zip(x,y):
	if(a==b):
		count+=1
cost=0
if(len(x)>len(y)):
	cost=len(x)-count
else:
	cost=len(y)-count
print(cost)