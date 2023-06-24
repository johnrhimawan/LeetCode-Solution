class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countmap = {}
        for substring in s:
            countmap[substring] = countmap.get(substring, 0) + 1

        for substring in t:
            countmap[substring] = countmap.get(substring, 0) - 1
        
        for item in countmap:
            if countmap[item] != 0:
                return False
        return True
