x,y=input().split()
cost=0
n=min(len(x),len(y))
for i in range(n):
  if len(y)==1 and y[0] in x:
    break
  if len(x)==1 and x[0] in y:
    break
  if x[i]!=y[i]:
    cost=cost+1
print(abs(len(x)-len(y))+cost)