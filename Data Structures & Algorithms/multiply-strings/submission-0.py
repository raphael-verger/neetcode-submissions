class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strToInt(num: str) -> int:
            res = 0
            # Iterate backwards to match powers of 10 with the correct place value
            power = 0
            for i in range(len(num) - 1, -1, -1):
                if num[i] == '0':
                    res += 0 * 10**power
                elif num[i] == '1':
                    res += 1 * 10**power
                elif num[i] == '2':
                    res += 2 * 10**power
                elif num[i] == '3':
                    res += 3 * 10**power
                elif num[i] == '4':
                    res += 4 * 10**power
                elif num[i] == '5':
                    res += 5 * 10**power
                elif num[i] == '6':
                    res += 6 * 10**power
                elif num[i] == '7':
                    res += 7 * 10**power
                elif num[i] == '8':
                    res += 8 * 10**power
                elif num[i] == '9':
                    res += 9 * 10**power
                power += 1

            return res

        def intToStr(num: int) -> str:
            if num == 0:
                return "0"

            res = ""
            while num > 0:
                digit = num % 10
                if digit == 0:
                    res = '0' + res
                elif digit == 1:
                    res = '1' + res
                elif digit == 2:
                    res = '2' + res
                elif digit == 3:
                    res = '3' + res
                elif digit == 4:
                    res = '4' + res
                elif digit == 5:
                    res = '5' + res
                elif digit == 6:
                    res = '6' + res
                elif digit == 7:
                    res = '7' + res
                elif digit == 8:
                    res = '8' + res
                elif digit == 9:
                    res = '9' + res

                num = num // 10

            return res

        int1 = strToInt(num1)
        int2 = strToInt(num2)
        product = int1 * int2
        return intToStr(product)
