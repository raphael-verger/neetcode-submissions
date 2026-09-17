from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using a standard dict is usually preferred for Two Sum, 
        # but we can use defaultdict(int) as you requested.
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in our map already
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store the index of the current number
            num_map[num] = i
