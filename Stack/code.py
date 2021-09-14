class stackNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.root=None
    def isEmpty(self):
        if self.root==None:
            return True
        else:
            return False
    def push(self,x):
        temp=stackNode(x)
        temp.next=self.root
        self.root=temp
        print("pushed element is %d"%x)
    def pop(self):
        if(self.isEmpty()):
            return "List is Empty."
        else:
            temp=self.root
            self.root=self.root.next
            print("Removed element is: %d"%temp.data)
    def peek(self):
        if(self.isEmpty()):
            return "List is empty"
        else:
            return "Top of stack is: %d"%self.root.data
    def DisplayStack(self):
        p=self.root
        while(p):
            print(p.data,end=" ")
            p=p.next
obj=stack()
for i in [1,2,3]:
    obj.push(i)
print(obj.peek())
obj.pop()
print(obj.peek())
print("Elements of stack is: ",end=" ")
obj.DisplayStack()
