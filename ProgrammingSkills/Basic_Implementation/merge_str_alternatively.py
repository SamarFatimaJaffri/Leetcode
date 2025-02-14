class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Find the minimum length between the two words to determine how many full pairs we can merge
        min_len = min(len(word1), len(word2))
        
        # Initialize an empty string to store the merged result
        mrg_str = ''
        
        # Iterate over the range of the smallest word length to alternate characters
        for i in range(min_len):
            # Add one character from word1 and one character from word2 to the result string
            mrg_str += f'{word1[i]}{word2[i]}'
        
        # Append the remaining characters from either word1 or word2 (whichever is longer) to the result string
        # The remaining part will be from the word that is longer, starting from index min_len
        return mrg_str + word1[min_len:] + word2[min_len:]
