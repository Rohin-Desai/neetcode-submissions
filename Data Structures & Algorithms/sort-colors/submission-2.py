class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r,w,b = 0,0,0
        for n in nums:
            if n == 0: r += 1
            if n == 1: w += 1
            if n == 2: b += 1
        k = 0
        for i in range(0, r):
            nums[k] = 0
            k += 1
        for i in range(0,w):
            nums[k] = 1
            k += 1
        for i in range(0,b):
            nums[k] = 2
            k += 1
