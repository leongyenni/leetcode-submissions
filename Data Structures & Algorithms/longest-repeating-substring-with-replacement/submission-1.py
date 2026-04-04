class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        window = 0
        maxF = 0
        left = 0

        for right, char in enumerate(s):
            count[char] = 1 + count.get(char, 0)
            maxF = max(maxF, count[char])

            while (right - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1

            window = max(window, right - left + 1)
           
        return window



        
                
