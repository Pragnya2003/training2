'''key=input()
key=key.replace(' ','')
s=''
for i in key:
    if i not in s:
        s=s+i
l=97
s1=''
for i in range(len(s)):
    s1=s1+chr(l)
    l=l+1
print(s1)'''

#dll
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            t.prev=None
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end='->')
            t=t.next
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end='->')
            t=t.prev
    def search(self,key):
        t=self.head
        s=self.tail
        f=0
        while(t!=None and s!=None):
            if(t.data==key or s.data==key):
               f=1
               break
            t=t.next
            s=s.prev
        if f==1:
            print('found')
        else:
            print('not found')
    def eor(self):
        t=self.head
        s=self.tail
        c=0
        while(t!=s):
            t=t.next
            s=s.prev
        if(t==s):
            print('even')
        else:
            print('odd')
    def palindrome(self):
        t=self.head
        s=self.tail
        f=1
        while(t!=s and t!=s.next):
            if(t.data==s.data):
                f=0
            else:
                f=1
                break
            t=t.next
            s=s.prev
        if f==0:
            print('palindrome')
        else:
            print('not a palindrome')
    def swap(self):#for even numbers only
        #method1
        t=self.head
        s=self.tail
        while(t.next!=s):
            t=t.next
            s=s.prev
        t=self.head
        while(s!=None):
            temp=node(t.data)
            t.data=s.data
            s.data=temp.data
            t=t.next
            s=s.next
        ----------------------
        #method2
        fast=self.head
        slow=self.head
        while(fast!=None):
            fast=fast.next.next
            slow=slow.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.next=None
        slow.prev=None
        self.head=slow
        self.tail=t1
l1=dll()
l1.addback(5)
l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(10)
l1.addback(12)
l1.addback(15)
l1.addfront(3)
#l1.addback(1)
l1.display()
print()
l1.swap()
l1.display()
#l1.rev_display()
print()
#l1.search(9)
#l1.eor()
#l1.palindrome()
