class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        num_array = []
        result = []
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for key in num_count:
            num_array.append(key)
        num_array.sort(key=lambda x: num_count[x], reverse=True)
        for i in range(k):
            result.append(num_array[i])
        return result
