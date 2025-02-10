class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize `first` and `second` to infinity to track the smallest and second smallest numbers
        first = second = float('inf')

        # Loop through each number in the list `nums`
        for num in nums:
            # If current number is smaller than `first`, save it in first
            if num <= first:
                first = num
            # If the current number is greater than `first` but not `second`, update `second`
            elif num <= second:
                second = num
            # If the current number is greater than both i.e., `first < `second` < `num`, return True
            else:
                return True
        
        # If no triplet is found after iterating through the entire list, return False
        return False
