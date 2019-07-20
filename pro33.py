s=input()
for i in range(len(s)):
	if(ord(s[i])>ord(s[0])):
		print(s[i:])
		break