class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        result = [1] * nums_length
        left = nums[0]
        for i in range(1, nums_length):
            result[i] *= left
            left *= nums[i]
        right = nums[nums_length - 1]
        for i in range(nums_length - 2, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result
