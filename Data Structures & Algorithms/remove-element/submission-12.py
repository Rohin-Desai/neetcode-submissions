class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        6:27pm
        """
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i