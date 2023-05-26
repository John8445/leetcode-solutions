class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        div = 1

        #increase divisor by multiples of ten until we can determine how large the number is
        while x > 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div
            #check if left digit = right digit
            if left !=right: return False

            #chop off the left and right digits
            x = (x% div) // 10
            #change the divisor by taking 2 digits away as well
            div = div/100

        return True