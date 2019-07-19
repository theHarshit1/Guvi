n=int(input())
p=2**n
for i in range(p):
	print(format(i,'0'+str(n)+'b')) 