class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        This function moves all the zeroes in the list `nums` to the end while maintaining the order of non-zero elements.
        """
        # Initialize a pointer 'i' to track the current position, and 'count0' to track the number of zeros moved
        i, count0 = 0, 0

        # Continue iterating until we've processed all elements, adjusting for the number of zeros moved
        while i < len(nums) - count0:
            # If the current element is zero, we need to move it to the end
            if nums[i] == 0:
                # Remove the element at index 'i' (which is zero)
                nums.pop(i)
                # Append zero to the end of the list
                nums.append(0)
                # Increment count0 to track how many zeros have been moved
                count0 += 1
            else:
                # If it's not a zero, just move the pointer to the next element
                i += 1
