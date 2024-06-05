#linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def add_end(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            t=self.head
            
            while(t.next!=None):
                t=t.next
            t.next=node(x)
    def add_front(self,x):
        t=self.head
        t1=node(x)
        t1.next=t
        self.head=t1
    def sum(self):
        t=self.head
        s=0
        while(t!=None):
            s=s+t.data
            t=t.next
        print('sum:',s)
    #searching key element from linked list
    def search(self,key):
        t=self.head
        f=0
        while(t.next!=None):
            if(t.data==key):
                f=1
                break
            t=t.next
        if(f==1):
            print('found')
        else:
            print('not found')
    #finding the middle element from even and odd lengths
    def middle(self):
        fp=self.head
        sp=self.head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next
        print(sp.data)
    def eor(self):
        fp=self.head
        sp=self.head
        while(fp!=None and fp.next!=None):
            sp=sp.next
            fp=fp.next.next
        if(fp==None):
            print('even')
        else:
            print('odd')
    def evensum(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
                t=t.next
        print(s)
    def los(self):
        c=1
        m=0
        t=self.head
        while(t.next!=None):
            if(t.data==t.next.data-1):
                c=c+1
                t=t.next
                if(m<c):
                    m=c
            else:
                c=1
                t=t.next
        print(m)
    #all pairs of linked list
    def pairs(self):
        i=self.head
        j=i.next
        while(i.next!=None):
            j=i.next
            while(j!=None):
                print(i.data,j.data)
                j=j.next
            i=i.next
    #selection sort
    def selsort(self):
        t=self.head
        t1=t.next
        while(t.next!=None):
            f=0
            t1=t.next
            while(t1!=None):
                if t.data>t1.data:
                    f=1
                    temp=node(t.data)
                    t.data=t1.data
                    t1.data=temp.data
                t1=t1.next
            if f==0:
                break
            t=t.next
        self.display()
    def bubblesort(self):
        t=self.head
        p=None
        while(t.next!=None):
            f=0
            t1=self.head
            while(t1.next!=p):
                if(t1.data>t1.next.data):
                    f=1
                    t1.data,t1.next.data=t1.next.data,t1.data
                t1=t1.next
            if f==0:
                break
            p=t1
            t=t.next
        self.display()
                    
            
                
l1=sll()
l2=sll()
l3=sll()
l1.add_end(10)
l1.add_end(20)
l1.add_end(30)
l1.add_end(40)
l1.add_end(60)
l1.add_front(50)
l3.add_front(8)
l3.add_end(2)
l3.add_end(4)
l3.add_end(3)
l3.add_end(7)
l3.add_end(6)
l3.add_end(1)
#l1.sum()
#l1.search(20)
#l2.add_end(400)
#l2.add_end(500)
#l2.add_end(600)
#l1.display()
#l3.display()
#print()
#l3.bubblesort()
#l3.selsort()
#print()
#l1.middle()
#l1.eor()
#l1.evensum()
#l3.display()
#l3.los()
#l3.pairs()
#l2.display()
