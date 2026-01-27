def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next: 
            return head
        temp = head.next 
        head.next = self.swapPairs(temp.next) 
        temp.next = head  
        return temp  
        
