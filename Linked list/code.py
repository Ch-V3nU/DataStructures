class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def DisplayList(self):
        temp=self.head
        while(temp):
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def addFirst(self,x):
        temp=Node(x)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
    def addLast(self,x):
        temp=Node(x)
        if self.head==None:
            self.head=temp
        else:
            p=self.head
            while(p.next):
                p=p.next
            p.next=temp
    def addAfter(self,x,val):
        temp=Node(x)
        p=self.head    
        while(p.data!=val):
            p=p.next
        t=p.next
        p.next=temp
        p.next.next=t
    def removeFirst(self):
        self.head=self.head.next
    def removeLast(self):
        p=self.head
        while(p.next.next!=None):
            p=p.next
        p.next=None
    def removeVal(self,x):
        if self.head.data==x:
            self.head=self.head.next
        else:
            p=self.head
            while(p.next.data!=x):
                p=p.next
            p.next=p.next.next
    def SortList(self):
        p=self.head
        q=None
        while(p):
            q=p.next
            while(q):
                if(p.data>q.data):
                    temp=p.data
                    p.data=q.data
                    q.data=temp
                q=q.next
            p=p.next
    def ReverseList(self):
        prev=None
        pres=self.head
        while(pres):
            Next=pres.next
            pres.next=prev
            prev=pres
            pres=Next
        self.head=prev
def getCount(List):
    cur=1
    if List.head==None:
        cur=0
    temp=List.head
    while(temp.next!=None):
        cur=cur+1
        temp=temp.next
    print(cur)
lis2=LinkedList()
for i in [10,15,30]:
    if(lis2.head==None):
        lis2.head=Node(i)
    else:
        temp=lis2.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(i)
print("Linked List: ")
lis2.DisplayList()
x=int(input("Enter the value to add at Beggining of linked LIst: "))
lis.addFirst(x)
lis.DisplayList()
y=int(input("Enter the value to add at Ending of linked list: "))
lis.addLast(y)
lis.DisplayList()
z=int(input("Enter value to add in linked list: "))
t=int(input("Enter the value of linked list to add new val after it: "))
lis.addAfter(z,t)
lis.DisplayList()
print("linked list after deletion of first node: ")
lis.removeFirst()
lis.DisplayList()
print("linked list after deletion of Lasf node: ")
lis.removeLast()
lis.DisplayList()
n=int(input("Enter val to remove in linked list: "))
lis.removeVal(n)
lis.DisplayList()
lis.SortList()
print("Linked list after sorting in ascending order: ")
lis.DisplayList()
lis.ReverseList()
print("Linked list after reversin the elements: ")
lis.DisplayList()
