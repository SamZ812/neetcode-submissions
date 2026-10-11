class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1

        result = []
        ans = []

        for x,y in counts.items():
            heapq.heappush(result, (y, x))
            if len(result) > k:
                heapq.heappop(result)


        for i in range(k):
            ans.append(heapq.heappop(result)[1])

        return ans