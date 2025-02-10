from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)

        # Return a list of booleans indicating whether each kid can have the greatest number of candies
        return [
            # For each kid's candy count, check if adding extraCandies results in having at least max_candies
            candy + extraCandies >= max_candies
            for candy in candies  # Loop through each kid's candy count in the list
        ]
