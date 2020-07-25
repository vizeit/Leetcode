# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists) -> ListNode:
    front, back = None, None
    while len(lists):
        d = [float('inf'),-1]
        if len(lists) > 1:
            for i in range(len(lists)):
                if lists[i] and lists[i].val < d[0]:
                    d[0] = lists[i].val
                    d[1] = i
                elif lists[i] is None:
                    del lists[i]
                    d[0] = float('inf')
                    break
            if d[0] != float('inf'):
                if front == None and back == None:
                    front = back = ListNode(d[0])
                else:
                    back.next = ListNode(d[0])
                    back = back.next
                lists[d[1]] = lists[d[1]].next
                if lists[d[1]] == None: del lists[d[1]]
        else:
            if lists[0]:
                if front == None and back == None:
                    front = lists[0]
                else:
                    back.next = lists[0]
            del lists[0]
    return front

if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = None
    l3 = ListNode(-1)
    out = mergeKLists([l1, l2, l3])
    while out:
        print(out.val)
        out = out.next