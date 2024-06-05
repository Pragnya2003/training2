'''#alphabet with given key
#ip:bvec
#n:4
#op:xray
k=input()
n=int(input())
s=''
for i in k:
    a=ord(i)-n
    while(a<97):
        a=97-a
        a=122-(a-1)
    s=s+chr(a)
print(s)

#method2:
k=input()
n=int(input())
c=n%26
s=''
for i in k:
    if((ord(i)-c)>=97):
        s=s+chr(ord(i)-c)
    else:
        s=s+chr(ord(i)-c+26)
print(s)

#ip:"xyzabcdefklmnopqefgh"
#op:7

n=input()
c=1
m=0
for i in range(len(n)-1):
    if(ord(n[i+1]) == ord(n[i])+1):
        c=c+1
        if(m<c):
            m=c
    else:
        c=1
print(m)

#ip:
  3
  xyz
  pqr
  abc
  "yraxpczqa"
  op:yes

n=int(input())
matrix=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(input())
    matrix.append(a)
str=input()
index=0
for i in str:
    if i in matrix[index]:
        flag=1
        index=index+1
        if(index==n):
            index=0
    else:
        flag=0
        break
if(flag==0):
    print('no')
else:
    print('yes')

#2

n=int(input())
matrix=[]
str=input()
for i in range(n):
    matrix.append(input())
for i in range(len(str)):
    if i not in m[i%n]:
        print('no')
else:
    print('yes')

#

n=int(input())
matrix=[]
for i in range(n):
    matrix.append(input())
str=input()
f=0
for i in range(len(str)):
    if(str[i] not in matrix[i%n]):
               print('no')
               f=1
               break
    else:
        matrix[i].remove(str[i])
if(f==0):
    print('yes')

#set doesn't allow sets list and dict and similar numbers shall be considered as one
#true and one will be duplicates
def recu(n,rev):
    if(n>0):
        rem=n%10
        rev=rev*10+rem
        return recu(n//10,rev)
    else:
        return rev
n=int(input())
m=n
s=recu(n,0)
if(s==m):
    print('palindrome')
else:
    print('not a palindrome')

#maxprofit O(n*n)
l=list(map(int,input().split()))
m=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        n=l[i]-l[j]
        if m>n:
            m=n
print(abs(m))

#O(n)
l=list(map(int,input().split()))
pr=0
b=l[0]
for i in range(len(l)):
    if b>l[i]:
        b=l[i]


#patterns

ip:5
op:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *

n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print('*',end=" ")
        else:
            print(k,end=" ")
            k=k+1
    print()

ip:4
op:
    ____a____
    ___aba___
    __abcba__
    _abcdcba_'''

a=int(input())
l=97
for i in range(a):
    for j in range(a-i):
        print("_",end='' )
    for k in range((2*i+1)):
        print(chr(l),end='')
        l=l+1
    l=97
    for k in range(a-i):
        print("_",end='' )
    print()

        










    
       
    






    
    
