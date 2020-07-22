# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    front, back = None, None
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                mv = l1.val
                l1 = l1.next
            else: 
                mv = l2.val
                l2 = l2.next
        elif l1:
            mv = l1.val
            l1 = l1.next
        else:
            mv = l2.val
            l2 = l2.next
        if front is None and back is None:
            front = ListNode(mv)
            back = front
        else:
            back.next = ListNode(mv)
            back = back.next
    return front
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    out = mergeTwoLists(l1, l2)
    while out:
        print(out.val)
        out = out.next