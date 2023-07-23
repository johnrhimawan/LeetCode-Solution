class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for (p, s) in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for pos, spd in pairs:
            dest_time = (target - pos) / spd
            if stack and stack[-1] >= dest_time:
                continue
            stack.append(dest_time)
        return len(stack)
