s=input()
m=0
j=0
for i in s:
	j+=1
	if(i=='c'):
		if(j>m):
			m=j
		j=0
print(max(j,m))
