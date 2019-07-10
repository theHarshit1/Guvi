n=int(input())
l=list(map(int,input().split()))
candies=n
c=[]
for i in range(len(l)):
	prev=l[i-1]
	next=