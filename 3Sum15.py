class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #stroe the result
        res = []

        #sort the array nlogn
        nums.sort()

        for i, a in enumerate(nums):

            #we dont wanna reuse the same value in the first portion of the array
            if i > 0 and a == nums[i-1]:
                continue
            
            #intitialize pointers for 2 sum portion
            l, r = i+1, len(nums)-1

            while l<r:
                
                threeSum = a + nums[l] + nums[r]

                #if sum > target=0 then deccrement right value to sum a smaller number to get to target
                if threeSum > 0:
                    r -= 1
                #else if sum < target = 0 then increment left pointer to get sum a bigger number
                elif threeSum < 0:
                    l += 1
                #lastly case 3 sum = target and store that result
                else:
                    res.append([a, nums[l], nums[r]]) 
                    #we are not done here we need to keep searching
                    #increment left pointer aka b to the next numnot the right pointer
                    l += 1

                    #moreover, keep shifting left pointer until weve reached next highest value and while l<r
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
