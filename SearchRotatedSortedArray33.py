class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Initialize two pointers for binary search
        left, right = 0, len(nums) - 1

        while left <= right:

            # Calculate the mid index
            mid = (left + right)//2

            # Check if the mid element is the target
            if target == nums[mid]:
                # If so, return the index
                return mid

            # Check if the left half is sorted (i.e., left element is less than or equal to mid element)
            if nums[left] <= nums[mid]:
                # If the target is greater than the mid element or less than the left element,
                # it means target is in the right half (unsorted part). For example, [5,6,7,1,2,3,4], mid=7, target=3, target>mid or target<5
                if target > nums[mid] or target < nums[left]:
                    # So, we move the left pointer to mid+1
                    left = mid+1
                # Otherwise, the target is in the left half (sorted part)
                else:
                    # So, we move the right pointer to mid - 1
                    right = mid - 1

            # If the left half is not sorted, then the right half is sorted
            else:
                # If the target is less than the mid element or greater than the right element,
                # it means target is in the left half (unsorted part). For example, [5,6,7,1,2,3,4], mid=1, target=5, target<mid or target>4
                if target < nums[mid] or target > nums[right]:
                    # So, we move the right pointer to mid - 1
                    right = mid - 1
                # Otherwise, the target is in the right half (sorted part)
                else:
                    # So, we move the left pointer to mid + 1
                    left = mid + 1

        # If we didn't find the target, return -1
        return -1
