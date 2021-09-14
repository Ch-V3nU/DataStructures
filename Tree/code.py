class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def Insert(self,data):
        temp=Node(data)
        if self.data:
            if data<=self.data:
                if self.left==None:
                    self.left=temp
                else:
                    self.left.Insert(data)
            elif(data>self.data):
                if self.right==None:
                    self.right=temp
                else:
                    self.right.Insert(data)
        else:
            self.data=data
    def Traversal(self):
        if self.left:
            self.left.Traversal()
        print(self.data,end=" ")
        if self.right:
            self.right.Traversal()
    def Inorder(self,root):
        if root:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    def Preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.Preorder(root.left)
            self.Preorder(root.right)
    def Postorder(self,root):
        if root:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.data,end=" ")
tree=Node(10)
for i in [1,2,3,2,66,3]:
    tree.Insert(i)
print("Tre Traversal: ",end="")
tree.Traversal()
print("\nInorder Traversal:",end=""),
tree.Inorder(tree)
print("\nPreoder Traversal: ",end="")
tree.Preorder(tree)
print("\nPostorder Traversal: ",end="")
tree.Postorder(tree)
print()
