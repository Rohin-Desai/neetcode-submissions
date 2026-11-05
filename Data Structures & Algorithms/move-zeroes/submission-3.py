class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        6:41pm
        """
        i = 0
        n = len(nums)
        k = 0
        while k < n and i < n:
            #move k to next non-zero
            while k < n and nums[k] == 0:
                k +=1
                if k == n:
                    return
            #now k points to non zero.
            if nums[i] == 0:
                nums[i],nums[k] = nums[k], nums[i]
                i += 1
            else:
                i += 1
                if k < i:
                    k = i

        