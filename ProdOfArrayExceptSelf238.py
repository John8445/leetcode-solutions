class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Initialize an output array and set it to 1
        result = [1] * len(nums)
        
        # Calculate the prefix product for each number
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Initialize the suffix product
        suffix = 1

        # Calculate the suffix product for each number and 
        # multiply it with the corresponding prefix product
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result