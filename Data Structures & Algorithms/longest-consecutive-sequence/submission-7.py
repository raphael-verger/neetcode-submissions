class Solution:

    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        consecutive = 1
        max_consecutive = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue  # Ignore duplicates
            elif nums[i + 1] == nums[i] + 1:
                consecutive += 1
            else:
                consecutive = 1

            max_consecutive = max(max_consecutive, consecutive)

        return max_consecutive
