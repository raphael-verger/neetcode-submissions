class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total_product=1
        for i in range(len(nums)):
            total_product*=nums[i]

        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(int(total_product/nums[i]))
            else:
                res.append(int(1))
                for j in range(len(nums)):
                    if j!=i:
                        res[i]*=nums[j]
        return res