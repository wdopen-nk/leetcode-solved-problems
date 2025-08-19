class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0

        minimum, maximum = -2**31, 2**31 - 1
        digits = list(str(x))
        reversedInteger = ''
        previousDigit = None
        
        while digits:
            symbol = digits.pop()
            if symbol == previousDigit == '0':
                continue
            if symbol == '-':
                reversedInteger = symbol + reversedInteger
            else:
                reversedInteger += symbol

        return int(reversedInteger) if minimum < int(reversedInteger) < maximum else 0


# s = Solution()
# print(s.reverse(123))
# print(s.reverse(-123))
# print(s.reverse(120))