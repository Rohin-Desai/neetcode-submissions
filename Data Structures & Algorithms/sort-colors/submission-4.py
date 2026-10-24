class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        4:42pm start
        Dutch flag problem
        lo mid hi
        before [0,lo), we have 0
        [lo, mid) white (1)
        [mid, hi] unsorted
        after (hi, len(nums)), we have 2
        """
        i = 0 #The low
        j = 0 # The mid
        k = len(nums) - 1 #our hi
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else: #nums[j] == 2
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1

        