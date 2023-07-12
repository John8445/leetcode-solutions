class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize curMax and curMin to handle the max and min product to 1
        # Initialize result to the max number in nums to handle the cases where all numbers are negative
        curMax, curMin = 1, 1
        result = max(nums)

        # Iterate over each number in nums
        for i in nums:

            # If current number is 0, reset the curMax and curMin to 1 and continue to the next iteration
            if i == 0:
                curMax, curMin = 1, 1
                continue

            # Store the curMax to tempMax because it will be updated, and we need the old value for updating curMin
            tempMax = curMax

            # Update curMax with the max of current number, current number * curMax and current number * curMin
            # This covers cases where multiplying with a negative number might give the max product
            curMax = max(i * curMax, i * curMin, i)

            # Update curMin similarly to curMax to handle cases where multiplying with a negative number gives min product
            curMin = min(i * tempMax, i * curMin, i)

            # Update result with max of result, curMax, and curMin to keep track of max product so far
            result = max(result, curMax, curMin)

        # Return the result which contains the max product of the subarray
        return result
