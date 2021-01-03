class Solution:
    def multiply(self, num1, num2):
        res = 0
        for i in range(1, len(num1) + 1):
            for j in range(1, len(num2) + 1):
                res += int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2)
        return str(res)