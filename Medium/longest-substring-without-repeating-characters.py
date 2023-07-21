class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        visited = set()
        begin = 0
        longest = 0
        for end in range(length):
            while s[end] in visited:
                visited.remove(s[begin])
                begin += 1
            visited.add(s[end])
            longest = max(longest, end - begin + 1)
        return longest


