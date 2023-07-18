class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        #declare pointers
        l, r = 0, len(numbers) - 1

        while l <= r:
            #get your current sum
            curSum = numbers[l] + numbers[r]

            #if the sum is greater than target shift right pointer to left
            #reason is our array is sorted so if we over shoot then num on right is too big
            # else our target is smaller than target so we need to shift the left pointer up
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1] 
        
        return[]

