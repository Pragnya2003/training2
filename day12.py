'''#breadth frst search
print('bfs:')
def bfs(d,x,q,v):
    q.append(x)
    while(q):
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        v.append(q.pop(0))
    print(v)
    
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
queue=[]
visited=[]
bfs(d,5,queue,visited)
-----------------------------------------------------------------
print('bfs:')
def bfs(d,x,q,v):
    q.append(x)
    while(q):
        for i in d[x]:
            if i not in q and i not in v:
                q.append(i)
        x=q[0]
        v.append(q.pop(0))
    print(v)
    
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
queue=[]
visited=[]
bfs(d,5,queue,visited)


#non cyclic graph
print('non cyclic graph')
def visit(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            visit(d,i)
    return
d={5:[7],7:[5,2,4],2:[7],4:[7,8],8:[4,6],6:[8]}
l=[]
visit(d,5)
print(l)

#dijkstras algorithm

def dij(g,d,x,q,v):
    q.append(x)
    d[x]=0
    while(q):
        m=9999
        for i in q:
            if d[i]<m:
                m=d[i]
                x=i
        for i in g[x]:
            if i[0] not in q and i[0] not in v:
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        v.append(x)
        q.remove(x)
    print(d)
    
g={5:[(8,2),(2,2),(3,2)],8:[(5,2),(3,3),(6,4)],6:[(8,4),(9,2)],9:[(6,2),(7,1),(4,2)],7:[(9,1),(3,3)],3:[(8,3),(2,1),(7,3)],2:[(5,2),(3,1)],4:[(9,2)]}
d={}
for i in g:
    d[i]=99999
vis=[]
queue=[]
dij(g,d,5,queue,vis)

ip:6 3 2 9 4 7
   8 7 5 3 6 9
op:[13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]
adding the even of list 1 and list 2 odd numbers

def fun(n1,n2,p,q,l):
    if p==len(n1):
        return l
    def fun2(n1,n2,p,q,l):
        if q==len(n2):
            return l
        else:
            if n1[p]%2==0:
                if n2[q]%2!=0:
                    x=n1[p]+n2[q]
                    l.append(x)
            q=q+1
            l=fun2(n1,n2,p,q,l)
            return l
    l=fun2(n1,n2,p,q,l)
    l=fun(n1,n2,p+1,q,l)
    return l

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
l=[]
print(fun(n1,n2,0,0,l))'''

#sum of frst iteration elements
def fun(n1,n2,p,q,l):
    if p==len(n1):
        return l
    def fun2(n1,n2,p,q,l):
        if q==len(n2):
            return l
        else:
            if n1[p]%2==0:
                if n2[q]%2!=0:
                    x=n1[p]+n2[q]
                    l.append(x)
            a=sum(l)
            q=q+1
            l=fun2(n1,n2,p,q,l)
            return l
    l=fun2(n1,n2,p,q,l)
    l=fun(n1,n2,p+1,q,l)
    return l

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
l=[]
print(fun(n

  

    
    
    
    































































































