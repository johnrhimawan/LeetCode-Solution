class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums) - 1

        while begin < end:
            mid = begin + (end - begin) // 2
            if nums[mid] > nums[end]:
                begin = mid + 1
            else:
                end = mid

        return nums[begin]
