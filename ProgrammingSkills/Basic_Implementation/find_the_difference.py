class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize two variables to store the cumulative sum of ASCII values of characters in 's' and 't'
        ord_s, ord_t = 0, 0
        
        # Iterate through the characters in 's' and 't' simultaneously using zip
        # We compute the sum of ASCII values for both strings up to the length of 's'
        for s_ch, t_ch in zip(s, t):
            ord_s += ord(s_ch)  # Add the ASCII value of the character in 's' to ord_s
            ord_t += ord(t_ch)  # Add the ASCII value of the character in 't' to ord_t

        # After the loop, 'ord_t' will have one extra character (the difference character in 't')
        # We need to add the ASCII value of the last character in 't' to ord_t
        ord_t += ord(t[-1])  # Add the ASCII value of the last character of 't' (the additional character)

        # The difference between the total sums of 't' and 's' will give the ASCII value of the extra character
        # Convert this difference back to a character using chr() and return it
        return chr(ord_t - ord_s)
