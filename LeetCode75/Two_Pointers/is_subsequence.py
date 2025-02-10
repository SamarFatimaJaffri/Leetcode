class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        This function checks if string 's' is a subsequence of string 't'.
        A subsequence of a string is obtained by deleting some or no characters 
        from the string without changing the order of the remaining characters.
        """
        # Initialize two pointers, one for each string
        ps, pt = 0, 0
        
        # Iterate through both strings using the pointers
        while ps < len(s) and pt < len(t):
            # If characters match at both pointers, move the pointer for 's' forward
            if s[ps] == t[pt]:
                ps += 1
            # Always move the pointer for 't' forward
            pt += 1
        
        # If all characters in 's' are matched in 't' (i.e., ps reaches the end of 's')
        return ps >= len(s)
