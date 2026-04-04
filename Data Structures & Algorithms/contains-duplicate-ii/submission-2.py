class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i, num in enumerate(nums):
            j = min(i + k, len(nums)-1)

            if j == i:
                break

            for i2 in range(i+1, j+1):
                if nums[i] == nums[i2]:
                    return True


        return False