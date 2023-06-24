class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        nums_length = len(nums)
        for i in range(nums_length):
            if (target - nums[i]) in mapping and mapping[target - nums[i]] != i:
                return [i, mapping[target - nums[i]]]
            mapping[nums[i]] = i