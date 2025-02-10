class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize two lists with [1] representing prefix and suffix of first and last number respectively
        prefix, suffix = [1], [1]

        # Iterate through each number
        for i in range(len(nums)-1):
            # multiply last number's prefix at prefix[-1] with number at current index
            # append the result to the end of prefix list
            prefix.append(prefix[-1] * nums[i])

            # multiply last number's suffix at suffix[0] with number at current index from back side
            # i.e., at -3 if current index is 2, and insert the result at the start of suffix list
            suffix.insert(0, suffix[0] * nums[-(i+1)])

        # multiply the prefix and suffix of each number to get the product of number except self
        return [prefix[i] * suffix[i] for i in range(len(nums))]
