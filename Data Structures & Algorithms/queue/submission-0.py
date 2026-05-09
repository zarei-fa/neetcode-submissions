class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self): # right=tail, left=head
        self.left = ListNode(None)
        self.right = ListNode(None)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False

    def append(self, value: int) -> None: # connect the new_node to dummy at the last step
        new_node = ListNode(value)
        self.right.prev.next = new_node
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev = new_node

    def appendleft(self, value: int) -> None: # connect the new_node to dummy at the last step
        new_node = ListNode(value)
        new_node.next = self.left.next
        self.left.next.prev = new_node
        self.left.next = new_node
        new_node.prev = self.left
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.right.prev.val
        target = self.right.prev
        target.prev.next = self.right
        self.right.prev = target.prev
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.left.next.val
        target = self.left.next
        self.left.next = target.next
        target.next.prev = self.left
        return val
