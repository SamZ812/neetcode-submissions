class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for i in nums:
            if i in counts:
                return True
            counts[i] += 1
        return False
