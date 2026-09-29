class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key = {}

        for n in nums:
            if n not in key:
                key[n] = 1
            else:
                return True

        return False
        