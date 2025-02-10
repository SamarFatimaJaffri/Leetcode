import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if str1 + str2 is the same as str2 + str1
        # This condition ensures that the two strings have a common repeating pattern
        if str1 + str2 != str2 + str1:
            return ''  # If they do not match, there's no common divisor string
        
        # Compute the greatest common divisor (GCD) of the lengths of str1 and str2
        len_gcd = math.gcd(len(str1), len(str2))

        # Return the substring of str1 from the start to the GCD length, which is the common divisor string
        return str1[:len_gcd]
