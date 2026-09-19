import bisect

class MedianFinder:

    def __init__(self):
        self.store = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.store, num)

    def findMedian(self) -> float:
        n = len(self.store)
        mid = n // 2
        
        if n % 2 == 1:
            return float(self.store[mid])
        else:
            return (self.store[mid - 1] + self.store[mid]) / 2.0
