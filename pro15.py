s=0
def binaryOnes(n):
   global s
   if n > 1:
       binaryOnes(n//2)
   s=s+(n % 2)
n=int(input())
l=list(map(int,input().split()))
ones=[]
for i in l:
	s=0
	binaryOnes(i)
	ones.append(s)
for i,x in sorted(zip(ones,l),reverse=True):
	print(x)