'''#hashing
hash function:h(k)=k%4
4,7,16,9,17,22

0   1   2   3
4   9   22  7
16  17

no collision occured are 22 and 7

#linear probing

0   1   2   3
4   16  9   7

#exceptional handling
try:
    a=[6,8,9]
    b='5'
    c=a[0]+b
    print(c)
#except ZeroDivisionError:
    print("zero")
except TypeError:
    print('invalid')
except:
    print('qw')
finally:
    print('end')

->adding integer and string will give typeerror
->int('t') this gives valueerror
->a={6:7,8:1} print(a[2]) will give key error
->a={4,6,7,8}
  a.append(7)
  print(a) will give attribute error
->a={4,6,7,8}
  a.remove(17)
  print(a) will give key error
->discard function will not give any errors if value is not present where as remove function will give error
->a={4,7,8,9}
  print(a[4]) will give typeerror
->a={4,7,8,9}
  a[0]=200
  print(a) will give typeerror:item cannot be assigned
->dict and set will remove duplicates
->set and list are heterogeneous
->list is not allowed in set because list are unhasbale and set also not allowed inside set
->set is mutable list and dict are mutable
->tuple and strings are immutable
->key in the dict should not be a list set and dict

#sort according to lengths of strings in a list
a=["school","car","apple","hi","hat"]
b=[]
for i in a:
    b.append(len(i))
c=list(zip(b,a))  #[(6,'school')
c.sort()
for i,j in c:
    print(j)

#sort with second element
def fun(x):
    return x[1]
a=[[3,15],[7,1],[2,8],[9,3],[5,6]]
a.sort(key=fun)
print(a)

#sort with sum of values
a=[[3,15],[7,1],[2,8],[9,3],[5,6]]
a.sort(key=sum)
print(a)

#sort with max
a=[[3,15],[7,1],[2,8],[9,3],[5,6]]
a.sort(key=max)
print(a)

#sort with min
a=[[3,15],[7,1],[2,8],[9,3],[5,6]]
a.sort(key=min)
print(a)'''


#kruskal's algorithm

d={5:[(2,2),(3,2),(8,2)],2:[(3,1),(5,2)],3:[(2,1),(5,2),(8,2),(7,3)],8:[(5,2),(3,3),(6,4)],6:[(8,4),(9,2)],7:[(3,3),(9,1)],9:[(6,2),(7,1),(4,2)],4:[(9,2)]}
def fun(q):
    return q[2]
def krus(i,c,v):
    q=[]
    


#prims algo
d={5:[(2,2),(3,2),(8,2)],2:[(3,1),(5,2)],3:[(2,1),(5,2),(8,2),(7,3)],8:[(5,2),(3,3),(6,4)],6:[(8,4),(9,2)],7:[(3,3),(9,1)],9:[(6,2),(7,1),(4,2)],4:[(9,2)]}
def fun(q):
    return q[2]
def prims(i,c,v):
     q=[]
     for j,k in d[i]:
         q.append((i,j,k))
     v.append(i)
     l=[]
     while q:
        q.sort(key=fun)
        if q[0][1] not in v:
         l.append(q[0])
         v.append(q[0][1])
         for i,j in d[q[0][1]]:
            if i not in v:
                q.append((q[0][1],i,j))
        q.pop(0)   
     print(l)
i=list(d.keys())[0]
prims(i,0,[])

























































































    
