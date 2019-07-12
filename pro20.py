n,k=map(int,input().split())
coins=list(map(int,input().split()))
coins=sorted(coins,reverse=True)
for i in range(len(coins)):
	c=0
	for j in coins[:i+1]:
		while(count<k):
			c+=1
			res.append(coins[j])
			count=coins[0]
		if(count==k):
			print(c)
			return
			
