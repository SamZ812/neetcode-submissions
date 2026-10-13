class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## [1, 2, 4, 6] example -> nums[1] = 1*4*6 = 24
        ## Prefix = [1, 1, 2, 8]
        ## Suffix = [48, 24, 6, 1] -> [48, 24, 6, 1]

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        result = [0] * len(nums)

        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            result[i] = suffix[i] * prefix[i]

        return result
