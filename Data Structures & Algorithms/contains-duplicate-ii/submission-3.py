class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i, num in enumerate(nums):
            j = min(i + k + 1, len(nums))

            if j == i:
                break

            for i2 in range(i+1, j):
                if nums[i] == nums[i2]:
                    return True

        return False