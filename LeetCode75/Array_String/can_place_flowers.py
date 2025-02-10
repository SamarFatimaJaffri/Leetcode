from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Get the length of the flowerbed array
        len_fb = len(flowerbed)
        
        # Iterate through the flowerbed to try placing flowers
        for i in range(len_fb):
            # If no more flowers need to be placed, return True
            if n <= 0:
                return True
            
            # Skip the position if it's already occupied by a flower
            if flowerbed[i] == 1:
                continue

            # Check if the previous position is empty or if it's the start of the flowerbed
            check_prev = i == 0 or flowerbed[i-1] == 0
            # Check if the next position is empty or if it's the end of the flowerbed
            check_next = i == len_fb - 1 or flowerbed[i+1] == 0
            
            # If both the previous and next positions are empty, we can place a flower here
            if check_prev and check_next:
                flowerbed[i] = 1  # Place a flower in the current position
                n -= 1  # Decrease the count of flowers left to be placed

        # If we've placed all required flowers, return True, otherwise return False
        return n <= 0
