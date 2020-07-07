class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    i, s = _subgetDecimalValue(head)
    return s

def _subgetDecimalValue(node):
    if node.next == None:
        return (1, 2**0 if node.val else 0)
    i, s = _subgetDecimalValue(node.next)
    return (i+1, s+2**i if node.val else s+0)

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    print(getDecimalValue(head))