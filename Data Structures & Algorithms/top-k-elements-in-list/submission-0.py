class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        result = []

        for key, value in counts.items():
            heapq.heappush(result, (value, key))
            if len(result) > k:
                heapq.heappop(result)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(result)[1])
        return ans





        