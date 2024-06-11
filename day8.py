'''#ip:[1,2,3,4,1,2,3,1,2]
#op:[[1 2 3 4],[1 2 3],[1 2]]
#ip:[2,3,1,3,4,3,2]
#op:[[2,3,1,4],[3,2],[3]]
def check(n,ou):
    l=[]
    k=[]
    if len(n)==0:
        return ou
    else:
        for i in n:
            if i not in l:
                l.append(i)
            else:
                k.append(i)
    ou.append(l)
    return check(k,ou)
n=list(map(int,input().split()))
ou=[]    
print(check(n,ou))

#print yes if input contain 26 letters
n=input()
m=n.replace(' ','')
s=[]
f=0
for i in m:
    if i not in s:
        s.append(i)
for i in s:
    if((ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90)):
        f=f+1
if(f==26):
    print('yes')
else:
    print('no')

#ip:"abfgresagtyuiofde"
#op:12

n=input()
d={}
s=''
m=0
i=0
while i<len(n):
    while i<len(n):
        if n[i] not in s:
            s=s+n[i]
            d[s[i]]=i
        else:
            if len(s)>m:
                m=len(s)
            s=''
            break
        i=i+1
    i=d[n[i]]+1
print(m)

#island
ip:
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6#
    op : 8
def fun(i,j):
    if (i<0 or j<0 or i>=n or j>=n):
        return
    if l[i][j]!=1:
        return 
    else:
        if l[i][j]==1:
            l[i][j]=0
        fun(i-1,j)
        fun(i,j-1)
        fun(i+1,j)
        fun(i,j+1)
    return
n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append((int(input())))
    l.append(a)
print()
r=int(input())
c=int(input())
fun(r-1,c-1)
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
print(count)'''

def fun(i,j,k,t):
    if k==len(s):
        return 1
    if (i<0 or j<0 or i>=n or j>=n):
        return
    if l[i][j]!=s[k]:
        return
    if l[i][j]==s[k]:
        l[i][j]=0
    if t!=1:
            t=fun(i-1,j,k+1)
            t=fun(i,j-1,k+1)
            t=fun(i+1,j,k+1)
            t=fun(i,j+1,k+1)
    return t 
n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append((input()))
    l.append(a)
print()
s=input()
for i in range(n):
    for j in range(n):
        if l[i][j]==s[0]:
            c=fun(i,j,1,0)
            if c==1:
                print('yes')
                break
if c==0:
    print('no')


'''class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if root==None:
            self.root=node(x)
        elif root.data>x:
            self.creat(root.left,x)
        else:
            self.creat(root.right,x)
            
t1=tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,20)
t1.creat(t1.root,7)
t1.creat(t1.root,1)'''

    
    
    

        
    






































