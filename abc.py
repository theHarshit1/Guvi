def insert(index,level):
    for i in range(n):
        if parents[i]==index:
            if len(nodes)<level+1:
                nodes.append([])
            nodes[level].append(i)
            insert(i,level+1)
t=int(input())
while(t!=0):
    n=int(input())
    parents=list(map(int,input().split()))
    nodes=[]
    for i in range(n):
        if parents[i]==-1:
            if len(nodes)<1:
                nodes.append([])
            nodes[0].append(i)
            insert(i,1)
    for i in nodes:
        print(*i)
        
