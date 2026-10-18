class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()
        
        target = 0

        for i in range(len(nums)):
            a = nums[i]
            ## a > 0 then only positives after, not possible
            if a > 0:
                break
            ## if nums[i] = the previous one this would be a duplicate
            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if a + nums[left] + nums[right] < target:
                    left += 1
                elif a + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
                

