import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        begin, end = 1, max(piles)
        min_k = end

        while begin <= end:
            mid = (begin + end) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)
            if totalTime <= h:
                if mid < min_k:
                    min_k = mid
                end = mid - 1
            else:
                begin = mid + 1
        return min_k

