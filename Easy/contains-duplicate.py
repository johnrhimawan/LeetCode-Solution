class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appear = set()
        for num in nums:
            if num in appear:
                return True
            appear.add(num)
        return False