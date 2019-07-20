s=input()
face=['r','t','l','b']
j=x=y=0
for i in s:
	if(i=='G'):
		if(face[j]=='r'):
			x+=1
		if(face[j]=='t'):
			y+=1
		if(face[j]=='l'):
			x-=1
		if(face[j]=='b'):
			y-=1
	elif(i=='R' and j>-4):
		j=j-1
	elif(i=='L' and j<3):
		j=j+1
	else:
		j=0
if x==0 and y==0:
	print("yes")
else:
	print("no")