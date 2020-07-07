class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    s = ''
    while head:
        s+=ascii(head.val)
        head = head.next
    return int(s,2)

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    print(getDecimalValue(head))