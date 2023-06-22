class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        #HashMap closed to open
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            #if we have a closing parenthesis
            if char in closeToOpen:
                #if stack not empty and top of stack via stack[-1] matches
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    #staack is empty or paren doesnt match
                    return False
            else:
                #we dont have a closing parenthesis we have an open one and we append to stak
                stack.append(char)
           
        return True if not stack else False