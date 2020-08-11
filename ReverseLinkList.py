from unittest import TestCase, main

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def toList(self):
        rs =[]
        while self: 
            rs.append(self.val)
            self = self.next
        return rs

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_reverseList(self):
        n = ListNode(3, ListNode(4, ListNode(5)))
        self.assertListEqual(self.solution.reverseList(n).toList(), [5,4,3])

if __name__ == "__main__":
    main()