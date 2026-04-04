class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1

        for key, count in countMap.items():
            if count > len(nums) // 3:
                res.append(key)

        return res
           