n=int(input())
l=list(map(int,input().split()))
a=l[:n//2]
b=l[n//2:]
if(sum(a)//len(a)==sum(b)//len(b)):
	print('yes')
	exit()
print('no')
