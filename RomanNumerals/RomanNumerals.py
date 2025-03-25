class Solution:
    def romanToInt(self, s: str) -> int:
        # define the roman numerals
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # set number to 0 to replace the roman numerals with their integer values
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

if __name__ == '__main__':
    s = Solution()

    x = "III"
    y = "LVIII"
    z = "MCMXCIV"

    print(s.romanToInt(x))
    print(s.romanToInt(y))
    print(s.romanToInt(z))
