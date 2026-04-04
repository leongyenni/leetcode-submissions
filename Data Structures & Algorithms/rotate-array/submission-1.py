class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        while k > 0:
            temp = nums[-1]
            temp2 = nums[0:-1]

            l = len(nums)

            nums[0:l] = [temp] + temp2

            k -= 1


        

        