class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = num + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[left], num, nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        
        return result
