class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        This function finds the maximum area of water that can be trapped between two vertical lines
        in the given list 'height' where each element represents the height of a vertical line at that index.
        The area is determined by the shorter of the two heights and the distance between them.
        """
        # Initialize the maximum area to 0
        area = 0
        # Initialize two pointers: one at the start (i) and one at the end (j) of the list
        i, j = 0, len(height) - 1
        
        # Use the two-pointer technique to explore the potential areas
        while i < j:
            # Calculate the area with the current pair of pointers and update the maximum area
            area = max(area, min(height[i], height[j]) * (j - i))
            
            # Move the pointer corresponding to the smaller height to potentially find a larger area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        # Return the maximum area found
        return max(area, min(height[i], height[j]) * (j - i))
