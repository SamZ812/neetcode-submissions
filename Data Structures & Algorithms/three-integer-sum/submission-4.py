class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first, sort the array
        nums.sort()
        target = 0
        result = []
        for i, a in enumerate(nums):
            # since it is sorted, if value > 0, no possible solution
            if a > 0:
                break
            # if a = previous a, we already checked this so move forward
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                if a + nums[left] + nums[right] < target:
                    left += 1
                elif a + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result
            