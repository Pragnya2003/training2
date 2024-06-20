'''#rain water trap
#ip:[2,5,2,3,6,7,1,0,5,7]
#op:20

h=list(map(int,input().split()))
l=h.copy()
r=h.copy()
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        l[i+1]=l[i]
print(l)       
for i in range(len(r)-1,-1,-1):
    if r[i]>r[i-1]:
        r[i-1]=r[i]
print(r)
s=0
for i in range(len(h)):
    s=s+abs(min(l[i],r[i])-h[i])
print(s)

#coins
def coin():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=list(map(int,input().split()))
n=int(input())
coin()

#ip:4x3
- - -
- - -
- - -
- - -
op:

def paths(i,j,c):
    if i<0 or i>=n or j<0 or j>=m:
        return c
    if i==n-1 and j==m-1:
        c=c+1
        return c
    v.append((i,j))
    if (i-1,j) not in v:
        c=paths(i-1,j,c)
    if (i,j-1) not in v:
        c=paths(i,j-1,c)
    if (i+1,j) not in v:
        c=paths(i+1,j,c)
    if (i,j+1) not in v:
        c=paths(i,j+1,c)
    #print(v)
    v.pop()
    return c
n=int(input())
m=int(input())
v=[]
print(paths(0,0,0))'''


#print paths for matrix above any obstruction present 
def paths(i,j,c):
    if i<0 or i>=n or j<0 or j>=m or (i==k and j==l):
        return c
    if i==n-1 and j==m-1:
        c=c+1
        return c
    v.append((i,j))
    if (i-1,j) not in v:
        c=paths(i-1,j,c)
    if (i,j-1) not in v:
        c=paths(i,j-1,c)
    if (i+1,j) not in v:
        c=paths(i+1,j,c)
    if (i,j+1) not in v:
        c=paths(i,j+1,c)
    #print(v)
    v.pop()
    return c
n=int(input())
m=int(input())
k=int(input())
l=int(input())
v=[]
print(paths(0,0,0))

        







































