class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        str_length = len(s)
        mappings = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(str_length):
            if s[i] == "I":
                if i < str_length - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
                    result -= mappings[s[i]]
                    continue
            if s[i] == "X":
                if i < str_length - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
                    result -= mappings[s[i]]
                    continue
            if s[i] == "C":
                if i < str_length - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
                    result -= mappings[s[i]]
                    continue
            result += mappings[s[i]]
        return result