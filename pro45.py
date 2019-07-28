s=input().strip('0')
mid=len(s)//2
if(len(s)%2!=0):
	s=s[:mid]+s[mid+1:]
if(s[:mid] == s[:mid-1:-1]):
	print("yes")
else:
	print("no")