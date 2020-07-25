# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists) -> ListNode:
    if not len(lists): return None
    elif len(lists) == 1: return lists[0]
    d = {}
    front = None
    while len(lists):
        i = 0
        while i < len(lists):
            if lists[i]:
                n = ListNode(lists[i].val)
                if lists[i].val not in d:
                    d[lists[i].val] = [n, n]
                else:
                    d[lists[i].val][1].next = n
                    d[lists[i].val][1] = n
                lists[i] = lists[i].next
            if lists[i] is None: 
                del lists[i]
                i -= 1
            i += 1
    for j in sorted(d.keys(),reverse=True):
        if front is None:
            front = d[j][0]
        else:
            d[j][1].next = front
            front = d[j][0]
    return front
            
if __name__ == "__main__":
    #mergeKLists([None, None, None])
    l1 = ListNode(2, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(7, ListNode(8, ListNode(9)))
    out = mergeKLists([l1, l2, l3])
    while out:
        print(out.val)
        out = out.next