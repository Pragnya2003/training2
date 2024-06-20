'''#nqueens
def queen(r):
    if r==n:
        return
    if r!=a:
        for c in range(n):
            if fun(r,c):
                m[r][c]='q'
                break
        return queen(r+1)
    else:
        queen(r+1)
    
def fun(i,j):
    if i==a:
        return 0
    elif j==b:
        return 0
    r=i;c=j
    for i in range(r+1):             #queen in column
        if m[i][j]=='q':
            return 0
    i=r
    while(i>=0 and j>=0):            #for left diagonal
        if m[i][j]=='q':
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):            #for right diagonal
        if m[r][c]=='q':
            return 0
        r=r-1
        c=c+1
    return 1
n=int(input())
a=int(input())
b=int(input())
m=[]
for i in range(n):
    m.append([0]*n)
queen(0)
print(m)
#print(m.count('q'))


#nqueens
def queen(r):
    if r==n:
        return
    for c in range(n):
        if fun(r,c):
            m[r][c]='q'
            break
        return queen(r+1)
    #queen(r+1)
    
def fun(i,j):
    r=i;c=j
    for i in range(r+1):             #queen in column
        if m[i][j]=='q':
            return 0
    i=r
    while(i>=0 and j>=0):            #for left diagonal
        if m[i][j]=='q':
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):            #for right diagonal
        if m[r][c]=='q':
            return 0
        r=r-1
        c=c+1
    return 1
n=int(input())
m=[]
for i in range(n):
    m.append([0]*n)
queen(0)
print(m)

#sunlight on building
l=list(map(int,input().split()))
left=l.copy()
right=l.copy()
for i in range(len(l)-1):
    if left[i]>left[i+1]:
        left[i+1]=left[i]
for i in range(len(l)-1,-1,-1):
    if right[i]>right[i-1]:
        right[i-1]=right[i]
print(list(set(left)))
print(list(set(right)))
    
#ip:[2,3,5,6]
#n=11
#op:yes
l=list(map(int,input().split()))
n=int(input())
s=0
f=0
for i in range(len(l)-1):
    for j in range(len(l)-1):
        s=sum(l[i:j+1])
    if s==n:
        f=1
        break
if f==1:
    print('yes')
else:
    print('no')
#-----------------------
#tabulation
l=list(map(int,input().split()))
n=int(input())
m=[]
for i in range(len(l)):
    l1=[0]*(n+1)
    m.append(l1)
for i in range(1,len(l1)+1):
    for j in range(n):
        if j==0:
            l1[i][j]=1
        if j<l[i]:
            l1[i][j]=l1[i-1][j]
        elif j==l[i]:
            l1[i][j]=1
        elif j>l[i]:
            x=j-l[i]
            l1[i][j]=l1[i-1][x]

#ip:tu5g2k1h8
   g5g8gd6h3
op:865312
s1=input()
s2=input()
l=''
for i in s1:
    if i.isdigit():
        l=l+i
for i in s2:
    if i.isdigit():
        l=l+i
k=[]
for i in l:
    if i not in k:
        k.append(i)
k.sort(reverse=True)
if int(k[-1])%2==0:
    print(''.join(k))
else:
    for i in range(len(k)-2,-1,-1):
        if int(k[i])%2==0:
            k.append(k.pop(i))
            print(''.join(k))
            break
        else:
            print(-1)

#ip:122 ip:121
#op:131 op:121

def palind(n,m):
    rev=0
    while n>0:
        x=n%10
        rev=(rev*10)+x
        n=n//10
    if rev==m:
        return rev
    else:
        return palind(m+1,m+1)

n=int(input())
m=n
print(palind(n,m))'''


n=int(input())
m=str(n)
if len(m)%2==0:
    x=m[:len(m)//2]
    if x+x[::-1]>n:
        print(x)
    else:
        







































            
            
        


























