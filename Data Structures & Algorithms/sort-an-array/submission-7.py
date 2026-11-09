class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        6:05pm
        """
        n = len(nums)
        i = 0
        j = n
        buf = [0 for _ in range(n)]
        return self.mergeSort(nums,i,j,buf)

    def mergeSort(self,nums, lo, hi, buf):
        mid = lo + (hi - lo)//2
        if hi - lo <= 1: #base case
            return nums
        self.mergeSort(nums, lo, mid, buf)
        self.mergeSort(nums, mid, hi, buf)
        self.merge(nums, lo, hi, buf)
        return nums
    
    def merge(self,nums, lo, hi, buf):
        mid = lo + (hi - lo)//2
        for z in range(lo,hi):
            buf[z] = nums[z]
        i = lo
        j = mid
        k = lo #index into nums
        while i < mid and j < hi:
            if buf[i] <= buf[j]:
                nums[k] = buf[i]
                i += 1
            else: 
                nums[k] = buf[j]
                j += 1
            k += 1
        while i < mid:
            nums[k] = buf[i]
            k += 1
            i += 1
        
