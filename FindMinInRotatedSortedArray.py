class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Handle base case: if there is only one element in the array
        if len(nums) < 2:
            return nums[0]

        # Another base case is a non-rotated sorted array ex. 1, 2, 3, 4, 5
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        
        # Initializing pointers for binary search
        low, high = 0, len(nums) - 1

        while low <= high:

            # Calculate the mid index
            mid = (low + high) // 2

            # If the mid element is less than the previous element, then the mid element is the smallest
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # If the mid element is greater than the next element, then the next element is the smallest
            if mid < len(nums) - 1 and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            # If middle element is greater than or equal to the last element,
            # the minimum must be in the right half (excluding mid), so move low to mid + 1
            if nums[mid] >= nums[high]:
                low = mid + 1

            # Else, the minimum must be in the left half, so move high to mid - 1
            else:
                high = mid - 1
            
        # The loop ended and we didn't find a peak which means the array is not rotated,
        # so the smallest value is the first element
        return nums[0]
