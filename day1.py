'''#merge two lists
n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
l=list()
i=0
j=0
while(i<len(n1) and j<len(n2)):
    if(n1[i]<n2[j]):
        l.append(n1[i])
        i=i+1
    else:
        l.append(n2[j])
        j=j+1
while(j<len(n2)):
    l.append(n2[j])
    j=j+1
while(i<len(n1)):
    l.append(n1[i])
    i=i+1
print(l)

#sliding window
n=input()
i=0
m=''
c=1
for i in range(len(n)-1):
    if(n[i]==n[i+1]):
        c=c+1
    else:
        m=m+n[i]+str(c)
        c=1
m=m+n[-1]+str(c) 
print(m)

#count the elements in list          
n1=list(map(int,input().split()))
l=[]
for i in n1:
    if(i not in l):
        l.append(i)
for i in l:
    print(i,"-",n1.count(i))


n=input()
uv,uc,lc,lv,d,s=0,0,0,0,0,0
l_v=['a','e','i','o','u']
u_v=['A','E','I','O','U']
for i in n:
    if(i.isupper() and i in u_v):
        uv=uv+1
    elif(i.islower() and i in l_v):
        lv=lv+1
    elif(i.isupper() and i not in u_v):
        uc=uc+1
    elif(i.isupper() and i not in l_v):
        lc=lc+1
    elif(i.isdigit()):
        d=d+1
    else:
        s=s+1
print('uv-',uv,'lv-',lv,'uc-',uc,'lc-',lc,'d-',d,'s-',s)

#upper to lower
n=input()
l=['a','e','i','o','u']
u=['A','E','I','O','U']
n1=''
for i in n:
    if i in l:
        i=i.upper()
        n1=n1+i
    elif i in u:
        i=i.lower()
        n1=n1+i
    else:
        n1=n1+i
print(n1)

#add even and odd
n1=input().split()
e,o,d=0,0,0
for i in n1:
    if '.' in i:
        d=d+i
    elif i.isOdd():
        o=o+i
    elif i.isinstance():
        d=d+i
print(e,o,d)

#numbers between 300 and 400
a=300
b=400
c=(b//7)-(a//7)
print(c)


#prime
n=int(input())
def prime(n):
    c=0
    for i in range(1,n//2):
        if n%i==0:
            c=c+1
    if c==1:
        return n
    else:
        return prime(n+1)    
s=prime(n)
print(s)

#
n=int(input())
while(1):
    c=0
    for i in range(1,n//2):
        if n%i==0:
            c=c+1
            break
    if c==1:
        print(n)
        break
    else:
        n=n+1

#num of primes in a number
n=int(input())
count=0
while(n):
    if(n%10 in[2,3,5,7]):
        count=count+1
    n=n//10
print(count)


#valid password
n=input()
u,l,s,d=0,0,0,0
for i in n:
    if i.isdigit():
        d=1
    elif i.isupper():
        u=1
    elif i.islower():
        l=1
    else:
        s=1
m=4-(u+l+s+d)
if (len(n)+m)<8:
    print(8-len(n))
elif len(n)==m:
    print(m)
else:
    print('-1')'''
        
    
        

        
        

            
    
