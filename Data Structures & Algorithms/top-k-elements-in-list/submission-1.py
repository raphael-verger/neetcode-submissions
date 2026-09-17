from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Initialize with 'int' so missing keys start at 0
        frequency_map = defaultdict(int)
        
        for num in nums:
            frequency_map[num] += 1

        # 2. Sort keys based on their values (frequency) in descending order
        # This creates a list of keys from highest frequency to lowest
        sorted_keys = sorted(frequency_map, key=frequency_map.get, reverse=True)

        # 3. Return the first k elements using a slice
        return sorted_keys[:k]
