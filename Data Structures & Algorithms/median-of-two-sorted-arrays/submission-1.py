class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        numsMerged = []
        nums1pointer = 0
        nums2pointer = 0

        # 1. Traverse up to the full length of each array
        while nums1pointer < len(nums1) and nums2pointer < len(nums2):
            if nums1[nums1pointer] < nums2[nums2pointer]:
                numsMerged.append(nums1[nums1pointer])
                nums1pointer += 1
            else:
                numsMerged.append(nums2[nums2pointer])
                nums2pointer += 1 

        # 2. Append whatever is left over using .extend()
        numsMerged.extend(nums1[nums1pointer:])
        numsMerged.extend(nums2[nums2pointer:])

        total_len = len(numsMerged)
        mid = total_len // 2

        # 3. Check if total length is odd, not if mid is odd
        if total_len % 2 == 1:
            return float(numsMerged[mid])
        else:
            return (numsMerged[mid - 1] + numsMerged[mid]) / 2.0
