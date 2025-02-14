class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort the input list to facilitate pairing elements
        nums.sort()

        # Initialize a counter for the number of operations
        op = 0
        
        # Two pointers: p1 starts from the beginning (0th index), p2 starts from the end (last index)
        p1, p2 = 0, len(nums) - 1
        
        # Continue while p1 is less than p2 (to ensure we're still checking pairs)
        while p1 < p2:
            num1 = nums[p1]  # Element at the left pointer (p1)
            num2 = k - num1  # Calculate the complement of num1 that sums to k

            # If num2 is equal to the element at the right pointer (p2), we've found a valid pair
            if num2 == nums[p2]:
                op += 1  # Increment the operation count
                # Move both pointers: p1 moves right, p2 moves left (both elements are now "used")
                p1, p2 = p1 + 1, p2 - 1
            # If num2 is larger than nums[p2], we need a larger element, so move p1 to the right
            elif num2 > nums[p2]:
                p1 += 1
            # If num2 is smaller than nums[p2], we need a smaller element, so move p2 to the left
            else:
                p2 -= 1
        
        # Return the total number of valid operations (pairs found)
        return op
