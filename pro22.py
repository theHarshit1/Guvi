s=[]
def maxSum(a):
	if(len(a)<1):
		return
	i=a.index(max(a))
	s.append(a[i])
	if(i!=0):
		maxSum(a[:i-1])
	maxSum(a[i+2:])

n=input()
l=[]
l=list(map(int,input().split()))
maxSum(l)
print(sum(s))