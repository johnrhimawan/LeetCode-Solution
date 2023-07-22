class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        expected = 0
        actual = 0
        for i in range(length):
            expected ^= i + 1
            actual ^= nums[i]
        return expected ^ actual
