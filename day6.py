#more occurence element
'''l=list(map(int,input().split()))
h=len(l)//2
for i in l:
    c=l.count(i)
    if c>h:
        f=i
print(f)

----------------------------
c=1
m=l[0]
for i in range(1,len(l)):
    if l[i]!=m:
        if c!=0:
            c=c-1
        else:
            m=l[i]
    else:
        c=c+1
print(m)

#leetcode268
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
k=(n*(n+1))//2
s=0
for i in l:
    s=s+i
print(k-s)

#largest out of kth number
n=int(input())
m=int(input())
a=[]
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
print(a[-m])

#coprimes
a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2+1)):
    if a%i==0 and b%i==0:
        print('ncp')
        break
    else:
        print('cp')'''


def balanced(s):
    st=[]
    f=0
    c=0
    for i in s:
        if i=='(' or i=='{' or i=='[':
            st.append(i)
        else:
            if not st:
                return False
            elif i==']' and st[-1]=='[':
                st.pop()
            elif i=='}' and st[-1]=='{':
                st.pop()
            elif i==')' and st[-1]=='(':
                st.pop()
            else:
                return c
                f=1
                break
    c=c+1
    if not st:
        return -1
    return st.index(i)

s=input()
print(balanced(s))
            



        
    


        
        
    

    

    
