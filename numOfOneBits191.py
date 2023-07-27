class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        while n > 0:
            temp = n % 2
            res = temp + res

            #bit shift to right
            n = n >> 1
        
        return res

        #faster but unnecessary version is below
        # res = 0 

        # while n:
        #     n &= (n-1)
        #     res += 1
        # return res



        
