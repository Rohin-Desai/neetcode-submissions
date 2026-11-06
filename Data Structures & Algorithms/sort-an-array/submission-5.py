class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        merge sort using a buffer. 
        8:12am
        """
        n = len(nums)
        lo, hi = 0, n  #Note, must be n not n-1
        mid = lo + (hi - lo)//2
        buf = [0 for _ in range(n)]
        self.mergeSort(nums,lo,hi,buf)
        return nums
        

    def mergeSort(self, nums: List[int], lo, hi, buf):
        if lo == hi:
            return 
        if hi - lo == 1: return 
        mid = lo + (hi - lo)//2
        self.mergeSort(nums,lo,mid,buf)
        self.mergeSort(nums,mid,hi, buf)
        self.merge(nums,lo,hi,buf)

    def merge(self,nums,lo,hi,buf):
        mid = lo + (hi - lo)//2
        i = lo
        j = mid
        k = lo #Index in nums
        #First copy range to buf. 
        for  t in range(lo,hi):
            buf[t] = nums[t]
        
        while i < mid and j < hi :
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

        
        
        
