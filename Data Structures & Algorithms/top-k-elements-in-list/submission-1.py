
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)

        result = []

        for i in nums:
            counts[i] += 1

        for key, value in counts.items():
            heapq.heappush(result, (value, key))
            if len(result) > k:
                heapq.heappop(result)

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(result)[1])
        return ans


        

        