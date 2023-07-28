class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m = len(nums1)
        n = len(nums2)
        length = m + n
        half = length // 2
        if len(B) < len(A):
            A, B = B, A

        begin, end = 0, len(A) - 1

        while True:
            mid = begin + (end - begin) // 2  # A
            other = half - mid - 2  # B

            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if (mid + 1) < len(A) else float('inf')
            Bleft = B[other] if other >= 0 else float('-inf')
            Bright = B[other + 1] if (other + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if length % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                else:
                    return min(Aright, Bright)
            
            if Aleft > Bright:
                end = mid - 1
            else:
                begin = mid + 1
