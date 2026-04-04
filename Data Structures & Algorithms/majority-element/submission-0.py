class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        maxCount = 0
        res = nums[0]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if maxCount < count[num]:
                maxCount = count[num]
                res = num

        return res