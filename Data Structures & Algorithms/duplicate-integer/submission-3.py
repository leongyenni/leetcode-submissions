class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key = set()

        for n in nums:
            if n in key:
                return True
            key.add(n)
        
        return False
        