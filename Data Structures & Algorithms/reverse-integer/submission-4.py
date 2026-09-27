class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True
        if x < 0 :
            isPositive = False
            x = -x
        res = ""
        for c in str(x):
            res = c + res
        if (abs(int(res))>=2**31 and not isPositive) or (abs(int(res))>=2**31-1 and isPositive):
            return 0
        return int(res) if isPositive else -int(res)

        