class Solution:
    def reverseWords(self, s: str) -> str:
        # Initialize an empty list to store the non-empty words
        words = []
        
        # Split the input string `s` by spaces and iterate through each word
        for word in s.split(' '):
            # If the word is empty (i.e., a result of multiple spaces), skip it
            if not word:
                continue

            # Append the non-empty word to the `words` list
            words.append(word)
        
        # Join the words in reverse order with a single space and return the result
        return ' '.join(words[::-1])
