'''#visiting all nodes of graph
print('visiting all nodes of graph')
def visit(d,x):
    l.append(x)
    for i in d[x]:
        if i not in l:
            visit(d,i)
    return
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
visit(d,5)
print(l)

#printing paths
print('printing paths')
def paths(d,x):
    l.append(x)
    if x==2:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            paths(d,i)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
paths(d,5)


#cost of paths
print('cost of paths')
def cost(d,x,c):
    l.append(x)
    if x==2:
        print(l,'-',c)
        l.pop()
        return c
    for i in d[x]:
        if i[0] not in l:
            cost(d,i[0],c+i[1])
    l.pop()
d={5:[(7,1),(3,2)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,7),(2,9)],8:[(3,8),(4,7),(2,6)],3:[(5,2),(7,5),(8,8)],2:[(4,9),(8,6)]}
l=[]
cost(d,5,0)

#shortest path cost
print('shortest path cost')
def minicost(d,x,c,m):
    l.append(x)
    if x==2:
        if c<m:
            m=c
        l.pop()
        return m
    for i in d[x]:
        if i[0] not in l:
            m=minicost(d,i[0],c+i[1],m)
    l.pop()
    return m
d={5:[(7,1),(3,2)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,7),(2,9)],8:[(3,8),(4,7),(2,6)],3:[(5,2),(7,5),(8,8)],2:[(4,9),(8,6)]}
l=[]
print(minicost(d,5,0,999999))

#shortest path and cost
print('shortest path and cost')
def pathndcost(d,x,e,c,m,l1):
    l.append(x)
    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=pathndcost(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
d={5:[(7,1),(3,2)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,7),(2,9)],8:[(3,8),(4,7),(2,6)],3:[(5,2),(7,5),(8,8)],2:[(4,9),(8,6)]}
l=[]
l1=0
print(pathndcost(d,5,2,0,999999,[]))

#all paths from initial node
print('all paths from initial node')
def paths(d,x,e):
    l.append(x)
    if x==e:
        print(l)
        l.pop()
        return
    for i in d[x]:
        if i not in l:
            paths(d,i,e)
    l.pop()
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
l=[]
for i in d.keys():
    paths(d,5,i)

#all shortest nodes path from initial node
print('shortest node path from initial node')
def pathndcost(d,x,e,c,m,l1):
    l.append(x)
    if x==e:
        if c<m:
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=pathndcost(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
d={5:[(7,1),(3,2)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,7),(2,9)],8:[(3,8),(4,7),(2,6)],3:[(5,2),(7,5),(8,8)],2:[(4,9),(8,6)]}
l=[]
l1=0
for i in d.keys():
    print(pathndcost(d,5,i,0,999999,[]))'''



































