class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)

        for i in nums:
            if counts[i]:
                return True
            counts[i] += 1
        return False