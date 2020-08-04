from unittest import TestCase, main

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mend, nend, rend = m-1, n-1, m+n-1
        while mend >=0 or nend >=0:
            if mend >=0 and nend >=0:
                if nums1[mend] < nums2[nend]:nums1[rend],nend=nums2[nend],nend-1
                else: nums1[rend],mend = nums1[mend],mend-1
            elif nend >=0:nums1[rend],nend=nums2[nend],nend-1
            elif mend >=0: break
            rend -= 1 

class testsolution(TestCase):
    def setUp(self):
        self.solution = Solution()
        self.inou = [
            ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
            ([8,50,70,0,0,0], 3, [8,50,70], 3, [8,8,50,50,70,70])
        ]
    def test_merge(self):
        for p1,p2,p3,p4,p5 in self.inou:
            with self.subTest(num1=p1,num2=p3,expected=p5):
                self.solution.merge(p1, p2, p3, p4)
                self.assertEqual(p1, p5)

if __name__ == "__main__":
    main()