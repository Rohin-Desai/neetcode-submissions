class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        solution by DRD
        2 pointer approach. 
        init last pointer to a non val position
        init a first pointer to the begining
        if first pointer points to a val than swap last pointer value with current place that first pointer points and move first pointer right and last pointer left and so on
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i = i + 1
        return n
    