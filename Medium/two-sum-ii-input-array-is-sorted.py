class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin = 0
        end = len(numbers) - 1
        while begin < end:
            sum = numbers[begin] + numbers[end]
            if sum == target:
                return [begin + 1, end + 1]
            if sum > target:
                end -= 1
            elif sum < target:
                begin += 1