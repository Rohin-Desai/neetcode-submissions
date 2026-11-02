class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        9:57pm
        """
        lo,hi = 0,len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if lo >= len(nums):
            return lo
        if nums[lo] == target:
            return lo
        if nums[lo] > target:
            return lo
        
        