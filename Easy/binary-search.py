class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = begin + (end - begin) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                begin = mid + 1
            else:
                return mid
        return -1

