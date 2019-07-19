def coinSum(index,count,s):
	if(s==v):
		print(count)
		return
	if(s<v):
		coinSum(index,count+1,s+coins[index])
		if index<len(coins)-1:
			coinSum(index+1,count+1,s)

n,v=map(int,input().split())
coins=sorted(list(map(int,input().split())),reverse=True)
coinSum(0,1,coins[0])
