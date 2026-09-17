from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = defaultdict(list)

        for num in nums:
            if (num_map[num].__contains__(1)):
                return True
            else :
                num_map[num].append(1)

        return False
        