class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Largest to smallest: add em up
        #smaller before larger: subtract the smaller

        roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }

        result = 0

        for i in range(len(s)):
        # if character after isnt out of bounds and the cur char is larger than next char we subtract the cur char
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:  
               result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result