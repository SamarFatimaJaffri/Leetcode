class Solution:
    def compress(self, chars: List[str]) -> int:
        # Get the length of the input list `chars`.
        n = len(chars)
        
        # Initialize two pointers: `i` to traverse the input list and `pointer` to track the new compressed string in place.
        i, pointer = 0, 0
        
        # Iterate through the list while `i` is less than `n` (end of the list).
        while i < n:
            # Set the current character `ch` and initialize the count of occurrences to 0.
            ch, count = chars[i], 0
            
            # Count how many times `ch` appears consecutively in the list.
            while i < n and ch == chars[i]:
                i, count = i + 1, count + 1
            
            # Store the character `ch` at the current `pointer` index and increment the pointer.
            chars[pointer] = ch
            pointer += 1

            # Check if the count is more than 1.
            if count > 1:
                # If the count is less than 10, just append the count as a single character.
                if count < 10:
                    chars[pointer] = str(count)
                    pointer += 1
                # If the count is 10 or greater, break the count into individual digits and append them.
                elif count > 1:
                    for num in str(count):
                        chars[pointer] = num
                        pointer += 1
        
        # Return the new length of the modified `chars` list, which is the `pointer` index.
        return pointer
