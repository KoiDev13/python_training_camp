class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        number = 0
        for i in range(len(s)-1):
            if romanDict[s[i]] < romanDict[s[i+1]] :
                number -= romanDict[s[i]] 
            else:
                number += romanDict[s[i]] 
        number += romanDict[s[len(s)-1]] 
        return number


print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))