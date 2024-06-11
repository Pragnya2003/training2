class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def creat(self,root,x):
        if self.root==None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif root.data>x:
            root.left=self.creat(root.left,x)
        else:
            root.right=self.creat(root.right,x)
        return root
    def preorder(self,root):
        if root==None:
            return
        else:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root==None:
            return
        else:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')
    def sum(self,root,s):
        if root:
            s=s+root.data+self.sum(root.left,s)+self.sum(root.right,s)
        return s
    def esum(self,root,es):
        if root:
            if root.data%2==0:
                es=es+root.data+self.esum(root.left,es)+self.esum(root.right,es)
            else:
                return self.esum(root.left,es)+self.esum(root.right,es)
        return es
    def osum(self,root,os):
        if root:
            if root.data%2!=0:
                os=os+root.data+self.osum(root.left,os)+self.osum(root.right,os)
            else:
                return self.osum(root.left,os)+self.osum(root.right,os)
        return os
    def eod(self,root):
        ''' x=self.esum(self.root,0)
        y=self.osum(self.root,0)
        return x-y'''
        if root:
            if root.data%2==0:
                return root.data+self.eod(root.left)+self.eod(root.right)
            return self.eod(root.left)+ self.eod(root.right)-root.data

        else:
            return 0
            '''if root.data%2!=0:
                os=os+root.data+self.osum(root.left,os)+self.osum(root.right,os)
            else:
                os=os+self.osum(root.left,os)+self.osum(root.right,os)
        return es-os'''
    def hot(self,root):
            if root==None:
                return -1
            return max(self.hot(root.left),self.hot(root.right))+1
    def bbt(self,root):
        return abs(self.hot(root.left)-self.hot(root.right))<=1
    def nol(self,root):
        if root==None:
            return
        if root.left==None and root.right==None:
            return 1
        return self.nol(root.left)+self.nol(root.right)
    '''#-------------------------------------------------------
    def nol(self,root,c):
        if root==None:
            return c
        if root.left==None and root.right==None:
            c=c+1
        c=self.nol(root.left)
        c=self.nol(root.right)
        return c'''
    def nolsum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data+self.nolsum(root.left)+self.nolsum(root.right)
        return self.nolsum(root.left)+self.nolsum(root.right)
    '''#----------------------------------------------------------------------------
    def nolsum(self,root,s):
        if root==None:
            return s
        if root.left==None and root.right==None:
            s=s+root.data
        s=self.nolsum(root.left,s)
        s=self.nolsum(root.right,s)
        return s'''
    def search(self,root,s):
        if root==None:
            return 0
        if root.data==s:
            return 1
        elif s<root.data:
            return self.search(root.left,s)
        else:
            return self.search(root.right,s)
        return
    def depth(self,root,y,c):
        if root==None:
            return -1
        if root.data==y:
            return c
        if root.data>y:
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
        return 
        
            
t1=tree()
t1.creat(t1.root,10)
t1.creat(t1.root,5)
t1.creat(t1.root,20)
t1.creat(t1.root,7)
t1.creat(t1.root,1)
print('preorder')
t1.preorder(t1.root)
print()
print('inorder')
t1.inorder(t1.root)
print()
print('postorder')
t1.postorder(t1.root)
print()
print()
print('sum of nodes')
print(t1.sum(t1.root,0))
print()
print('difference btw left and right subtree')
print(abs(t1.sum(t1.root.left,0)-t1.sum(t1.root.right,0)))
print()
print('evensum')
print(t1.esum(t1.root,0))
print()
print('oddsum')
print(t1.osum(t1.root,0))
print()
print('abs difference')
print(t1.eod(t1.root))
print()
print('height of tree')
print(t1.hot(t1.root))
print()
print('balanced or not')
if t1.bbt(t1.root):
    print('balanced')
else:
    print('not balanced')
print()
print('no of leaf nodes')
print(t1.nol(t1.root))
print()
print('sum of leaf nodes')
print(t1.nolsum(t1.root))
print()
print('search for an element')
s=int(input())
if t1.search(t1.root,s)==1:
    print('found')
else:
    print('not found')
print()
print('depth of tree')
y=int(input())
print(t1.depth(t1.root,y,0))



























             
