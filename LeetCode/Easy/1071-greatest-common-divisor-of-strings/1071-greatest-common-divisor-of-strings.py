class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # x divdes str1 > str1 = x + x + ... x
        if (str1 + str2) != (str2 + str1):
            return ""
        
        a, b = len(str1), len(str2)
        while b != 0:
            a, b = b, a % b
        
        return str1[:a]