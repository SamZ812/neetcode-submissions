class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0

        nums.sort()

        result = []

        for index, value in enumerate(nums):

            if value > 0:
                break 

            if index > 0 and value == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                if target < value + nums[left] + nums[right]:
                    right -= 1
                elif target > value + nums[left] + nums[right]:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result