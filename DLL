class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createDoublyLinkedList(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
arr=list(map(int,input().split()))
print(createDoublyLinkedList(arr))


Output:
1 2 3 4
None
