class MyLinkedList:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1
            
        temp = self.head
        while temp:
            if index == 0:
                return temp.val
            temp = temp.next
            index -= 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = MyLinkedList(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return 

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        
        new_node = MyLinkedList(val)
        self.tail.next = new_node
        self.tail = new_node 
        return 

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        
        temp = self.head
        while temp:
            if index == 1:
                new_node = MyLinkedList(val)
                new_node.next = temp.next
                temp.next = new_node
                
                if not new_node.next:
                    self.tail = new_node
                return
            
            temp = temp.next
            index -= 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return

        temp = self.head
        while temp:
            if index == 1 and temp.next:
                temp.next = temp.next.next
                
                if not temp.next:
                    self.tail = temp
                return
            
            temp = temp.next
            index -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)