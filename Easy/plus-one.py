class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry == 10:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits
