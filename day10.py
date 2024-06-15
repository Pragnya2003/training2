'''#ip:[4,8,14,22,36,68]
#print sum of largest primes between two elements of array
def prime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+1
    if c==1:
        return True
    else:
        return False

l=list(map(int,input().split()))
m=[]
for i in range(len(l)-1):
    j=i+1
    for k in range(l[j]-1,l[i],-1):
        x=prime(k)
        if x:
            m.append(k)
            break
print(sum(m))

#ip:[4 9 8 2 14 3 5 6]
4 9 8 2 14 3 5 6
4 8 9 2 14 3 5 6
  2 8 9 14 3 5 6
    8 9 14 3 5 6
      3 9 14 5 6
        5 9 14 6
          6  9 14
4 2 8 3 5 6 9 14
                
l=list(map(int,input().split()))
for i in range(len(l)):
    j=i+2
    k=l.index(min(l[i:j+1]))
    l[k],l[i]=l[i],l[k]
print(l)

ip:"hello:5438,car:214,book:8799,apple:2187"
op:oaxp

s1=input()
s2=s1.split(',')
s=''
for i in s2:
    b=i.split(':')
    l=len(b[0])
    if str(l) in b[1]:
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if str(i) in b[1]:
                s=s+b[0][i-1]
                break
        else:

            s=s+'x'
print(s)'''
                                 
                           
            

    
    
    
        
        

            
            
        
        
        
