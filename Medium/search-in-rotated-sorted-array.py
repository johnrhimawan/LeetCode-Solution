class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            if nums[begin] <= nums[mid]:
                if nums[mid] < target or nums[begin] > target:
                    begin = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] > target or nums[end] < target:
                    end = mid - 1
                else:
                    begin = mid + 1

        return -1
