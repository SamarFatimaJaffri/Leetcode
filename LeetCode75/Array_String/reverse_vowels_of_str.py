class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the input string into a list of characters so we can modify it in place
        s_arr, vowels = list(s), 'aeiou'
        
        # Initialize two pointers, i at the beginning and j at the end of the string
        i, j = 0, len(s) - 1
        
        # Loop until the two pointers cross each other
        while i < j:
            # Move pointer i forward if the character at i is not a vowel
            if s_arr[i].lower() not in vowels:
                i += 1
                continue  # Skip the rest of the loop and go to the next character
            
            # Move pointer j backward if the character at j is not a vowel
            if s_arr[j].lower() not in vowels:
                j -= 1
                continue  # Skip the rest of the loop and go to the next character
            
            # Swap the vowels at the i-th and j-th positions
            s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
            
            # Move both pointers towards each other
            i, j = i + 1, j - 1
        
        # Convert the list of characters back into a string and return it
        return ''.join(s_arr)
