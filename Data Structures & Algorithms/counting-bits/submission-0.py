class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n+1)
        for i in range(0,n+1):
            output[i]=bin(i).count('1')

        return output

        