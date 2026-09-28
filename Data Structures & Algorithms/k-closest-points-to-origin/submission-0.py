class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(minHeap, (dist, [x,y]))

        for i in range(k):
            point = heapq.heappop(minHeap)[1]
            res.append(point)

        return res