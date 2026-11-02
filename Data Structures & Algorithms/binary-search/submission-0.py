class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        9:35pm-
        """
        lo = 0
        hi = len(nums)
        res = -1
        while(lo < hi):
            mid = lo + (hi - lo)//2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        
        if lo >= len(nums):
            return -1
        if nums[lo] == target:
            return lo
        return -1