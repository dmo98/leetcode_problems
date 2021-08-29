class Node:
    def __init__(self, data, next_node=None, prev_node = None):
        self.val = data
        self.next = next_node
        self.prev = prev_node


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length or self.head is None:
            return -1
        
        current_node = self.head
        position = index
        while position > 0:
            current_node = current_node.next
            position -= 1
        return current_node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(data=val, next_node=self.head)
        self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.length == 0:
            new_node = Node(data=val)
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            new_node = Node(data=val, prev_node=current_node)
            current_node.next = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.length:
            return None

        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(data=val)

            position = index
            current_node = self.head

            while position > 1:
                current_node = current_node.next
                position -= 1

            previous_node = current_node
            next_node = current_node.next
            
            new_node.prev = previous_node
            new_node.next = next_node

            previous_node.next= new_node
            if next_node is not None:
                next_node.prev = new_node
            
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            new_head = self.head.next
            if new_head is not None:
                new_head.prev = None
            self.head = new_head
            self.length -= 1
        else:
            position = index
            current_node = self.head

            while position > 1:
                current_node = current_node.next
                position -= 1

            previous_node = current_node
            deleted_node = current_node.next
            next_node = deleted_node.next

            previous_node.next = next_node
            if next_node is not None:
                next_node.prev = previous_node
            self.length -= 1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)