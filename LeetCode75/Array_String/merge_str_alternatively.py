class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Determine the minimum length between the two words
        min_len = min(len(word1), len(word2))

        # Initialize an empty string to store the merged result
        word = ''

        # Loop through each character up to the minimum length
        for i in range(min_len):
            # Add characters alternately from word1 and word2
            word += f'{word1[i]}{word2[i]}'

        # Append any remaining characters from word1 or word2 (if one is longer)
        return word + word1[min_len:] + word2[min_len:]
