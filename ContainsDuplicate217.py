class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()  # Create an empty set
        for num in nums:  # Iterate over the array
            if num in num_set:  # If the number is already in the set
                return True  # There is a duplicate
            num_set.add(num)  # Add the number to the set
        return False  # No duplicates found