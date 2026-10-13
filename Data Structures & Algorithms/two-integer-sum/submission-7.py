class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        for i in range(len(nums)):
            if target - nums[i] in counts:
                return [counts[target - nums[i]], i]
            counts[nums[i]] = i
    