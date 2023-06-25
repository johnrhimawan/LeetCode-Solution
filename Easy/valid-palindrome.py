class Solution:
    def isPalindrome(self, s: str) -> bool:
        begin = 0
        end = len(s) - 1
        s = s.lower()
        while begin < end:
            begin_string = s[begin]
            end_string = s[end]
            if not begin_string.isalnum():
                begin += 1
                continue
            if not end_string.isalnum():
                end -= 1
                continue
            if begin_string != end_string:
                return False
            begin += 1
            end -= 1
        
        return True