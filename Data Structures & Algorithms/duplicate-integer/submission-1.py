class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for num in nums:
            if counts[num]:
                return True
            counts[num] += 1
        return False