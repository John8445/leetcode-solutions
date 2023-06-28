class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        newString = ""

        if len(word1) < len(word2):
            for i in range(len(word1)):
                newString += word1[i]
                newString += word2[i]
            newString += word2[len(word1):]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                newString += word1[i]
                newString += word2[i]
            newString += word1[len(word2):]
        else:
            for i in range(len(word2)):
                newString += word1[i]
                newString += word2[i]
        
        return newString