class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        6:11pm
        """
        n = len(nums)
        i = 2
        j = 2
        while j < n:
            if nums[i-2] == nums[j] and nums[i-1] == nums[j]:
                j += 1
            else:
                nums[i] = nums[j]
                j += 1
                i += 1
        return i