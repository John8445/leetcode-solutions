class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        #base case n=0 or 1
        if x == 0 or x == 1:
            return x

        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) // 2

            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right