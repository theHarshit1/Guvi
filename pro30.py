n=input()
for i in range(len(n)):
	if(int(n[:i]+n[i+1:])%8==0):
		print('yes')
		exit()
print('no')