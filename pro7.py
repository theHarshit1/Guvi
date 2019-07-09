n=int(input())
p=1
powers=[]
powers.append(p)
while p<n:
	p*=2
	powers.append(p)
for i in range(len(powers)):
	if(powers[i]<n):
		p=i
	else:
		break
diff=0
if(n-powers[p]<powers[p+1]-n):
	diff=n-powers[p]
else:
	diff=powers[p+1]-n
print(diff)
