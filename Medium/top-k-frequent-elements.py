class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = [0] * max(nums)
        for num in nums:
            num_count[num] += 1
        
        sorted_count = sorted(num_count, reverse=True)

        count = 0
        result = []
        for item in sorted_count:
            result.append(num_count.index(item))

