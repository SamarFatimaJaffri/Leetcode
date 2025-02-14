class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize max_sum and curr_sum to the sum of the first k elements.
        # This sets the first window sum as the starting point.
        max_sum = curr_sum = sum(nums[:k])  
        
        # Set the two pointers: i starts at 1 (next element after the first window), and j starts at k (just after the first window).
        i, j = 1, k
        
        # Slide the window until j reaches the end of the list.
        while j < len(nums):
            # Update the current window sum by sliding the window:
            # Subtract the element at i-1 (left side, leaving the window) and add the element at j (right side, entering the window).
            curr_sum = curr_sum - nums[i-1] + nums[j]
            
            # If the new sum is greater than the previous maximum, update max_sum.
            if curr_sum > max_sum:
                max_sum = curr_sum
                
            # Move the pointers forward: i increments to slide the window from the left side, and j increments to expand the window to the right.
            i, j = i + 1, j + 1
        
        # Return the maximum sum divided by k to get the average of the subarray with the maximum sum.
        return max_sum / k
