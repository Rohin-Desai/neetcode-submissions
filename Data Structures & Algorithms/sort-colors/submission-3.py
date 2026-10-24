class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        use djikstra's dutch flag algol
        solution by DRD on 10/15/2026
        """
        i = 0
        j = 0
        k = len(nums) - 1

        while j <= k:
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                #swap nums[i] and nums[j]
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            else: # nums[j] == 2:
                nums[j],nums[k] = nums[k],nums[j]
                k -= 1





        