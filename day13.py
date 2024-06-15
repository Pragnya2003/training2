'''#nums:times [(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
#costs:[5,6,5,4,11,2]
#job scheduling

nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
cost=[5,6,5,4,11,2]
l=cost.copy()
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[i][0]>=nums[j][1]:
            if l[j]+cost[i]>l[i]:
                l[i]=l[j]+cost[i]
print(max(l))


ip:asabab
   baabab
   longest common subsequence

ip:abcd
   axbdc
op:abc

s1=input()
s2=input()
s=''
m=[]
u=len(s1)
v=len(s2)
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            m[i][j]=m[i-1][j-1]+1
            
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
while(u!=0 and v!=0):
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if m[u][v]==m[u-1][v]:
            u=u-1
        else:
            v=v-1
print(s[::-1])

#island
def area(i,j,a):
    if m[i][j]==1:
        a=a+1
        m[i][j]=0
    else:
        return a
    if i+1<n:
        a=area(i+1,j,a)
    if i-1>0:
        a=area(i-1,j,a)
    if j+1<n:
        a=area(i,j+1,a)
    if j-1>0:
        a=area(i,j-1,a)
    return a

m=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=5
s=0
a=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            r=area(i,j,0)
            if r>a:
                a=r
print(a)

#7262 sec ---> 2hr: 1min: 2sec
n=int(input())
x=n//3600
x1=n%3600
y=x1//60
y1=x1%60
print(x,'h:',y,'m:',y1,'s:')

#coins

l=list(map(int,input().split()))
n=int(input())

#ip:360days in a year 30days in month 6days in week
#ip:65476
#op:?years ?months ?weeks ?days

n=int(input())
x=n//360
x1=n%360
y=x1//30
y1=x1%30
z=y1//6
a=y1%6
print(x,'years',y,'months',z,'weeks',a,'days')'''
































