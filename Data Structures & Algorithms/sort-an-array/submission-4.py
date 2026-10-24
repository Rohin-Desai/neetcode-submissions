class Solution:
    """
    Provide solution without using sublists
    solution by DRD 
    See this link for a discussion:
    https://share.gemini.google/H5EYdydoJxnN
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums)
        buffer = [0] * hi
        self.mergeSort(nums, 0, hi, buffer )
        return nums
        
    def mergeSort(self, nums, lo, hi, buffer): #No return. nums is sorted array.
        mid = lo + (hi-lo)//2
        if lo == hi: return
        if hi-lo == 1: return
        self.mergeSort(nums, lo, mid, buffer)
        self.mergeSort(nums, mid, hi, buffer)
        self.merge(nums, lo, hi, buffer)

    def merge(self, nums, lo, hi, buffer):
        mid = lo + (hi-lo)//2
        i = lo #index for first half in nums
        j = mid #index for second half in nums
        k = lo 
        
        for t in range(lo,hi):
            buffer[t] = nums[t]

        while i < mid and j < hi:
            if buffer[i] <= buffer[j]:
                nums[k] = buffer[i]
                i += 1
            else:
                nums[k] = buffer[j]
                j += 1
            k += 1

        while i < mid:
                nums[k] = buffer[i]
                k += 1
                i += 1
       

                
        