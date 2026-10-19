class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## time to get to end = target - position / speed

        ## if current car takes less time then one before it, they will both reach target at the same time, so pop the current one to not duplicate groups

        stack = []

        paired = [(p,s) for p,s in zip(position, speed)]
        paired.sort(reverse=True)

        for pos, speed in paired:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()
        return len(stack)
