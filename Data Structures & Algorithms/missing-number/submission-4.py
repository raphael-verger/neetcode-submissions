class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # The sum we expect if no numbers were missing
        expected_sum = n * (n + 1) // 2
        # The actual sum of the elements present
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum
