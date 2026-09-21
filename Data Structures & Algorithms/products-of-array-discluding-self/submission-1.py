class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt=0
        res = [0]*len(nums)
        product=1
        for i in range(len(nums)):
            if nums[i]==0:
                zero_cnt+=1
            else: 
                product*=nums[i]
        
        if zero_cnt>1 : return res

        res = [0]*len(nums)
        if zero_cnt==0:
            for i in range(len(nums)):
                res[i]=int(product/nums[i])

        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    res[i]=product

        return res

            

