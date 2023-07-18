class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def generate(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                generate(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                generate(openN, closeN + 1)
                stack.pop()

        generate(0, 0)
        return result
    
