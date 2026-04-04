class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0: return word2
        if len(word2) == 0: return word1

        result = ""

        if len(word1) > len(word2):
            m = len(word2) 
        else:
            m = len(word1)

        i = 0
        while i < m:
            result += word1[i]
            result += word2[i]
            i += 1

        if len(word1) > len(word2):
            result += word1[i:]
        elif len(word2) > len(word1):
            result += word2[i:]

        return result

        
