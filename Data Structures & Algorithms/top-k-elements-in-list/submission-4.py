class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1

        heap = []

        ## place counts in a heap, remove if past length of desired answer

        for item, count in counts.items():
            heapq.heappush(heap, (count, item))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result