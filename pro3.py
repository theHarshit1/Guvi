x,y=input().strip().split(" ")
max=[]
f=0
for i in range(len(y)):
	prev=0
	l=[]
	for j in y[i:]:
		for k in range(prev,len(x)):
			if(j==x[k]):
				l.append(k)
				prev=k+1
				break
	if(len(l)>len(max)):
		max=l
res=x[max[0]:max[len(max)-1]+1]
cost=len(x)-len(res)
print(cost)
print(len(y)-len(res)+cost)