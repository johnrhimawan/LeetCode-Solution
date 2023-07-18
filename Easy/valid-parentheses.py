class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if mapping[curr] != char:
                    return False
        return not stack
