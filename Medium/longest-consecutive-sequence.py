class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_sequence = 0
        for num in nums:
            if (num - 1) not in hashset:
                length = 1
                while (num + length) in hashset:
                    length += 1
                max_sequence = max(max_sequence, length)
        return max_sequence