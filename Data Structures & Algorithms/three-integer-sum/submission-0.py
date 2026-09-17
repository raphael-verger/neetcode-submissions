class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == -nums[i]:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < -nums[i]:
                    left += 1
                else:
                    right -= 1

        return [list(t) for t in result]
