s=input()
d="dhoni"
if(len(s)!=len(d)):
	print('no')
	exit()
for i in s:
	if(i not in d):
		print('no')
		exit()
	d=d.replace(i,'')
print('yes')