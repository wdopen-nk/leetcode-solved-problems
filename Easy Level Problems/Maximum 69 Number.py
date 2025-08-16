class Solution:
    def maximum69Number (self, num: int) -> int:
        digitArray = list(str(num))
        for i, digit in enumerate(digitArray):
            if digit == '6':
                digitArray[i] = '9'
                break
        return int(''.join(digitArray))

# s = Solution()
# print(s.maximum69Number(9696))
# print(s.maximum69Number(9996))
# print(s.maximum69Number(9999))