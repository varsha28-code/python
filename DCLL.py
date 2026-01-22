class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createDCLL(arr):
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
    temp.next=head
    head.prev=temp
arr=list(map(int,input().split()))   
print(createDCLL(arr))


Output:
1 2 3 4
None
