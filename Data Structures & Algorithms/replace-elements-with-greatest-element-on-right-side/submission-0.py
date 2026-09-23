class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [-1] * len(arr)

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] > result[i]:
                    result[i] = arr[j]
        return result
