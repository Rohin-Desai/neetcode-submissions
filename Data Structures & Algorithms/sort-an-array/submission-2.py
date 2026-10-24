class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self,nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        lo,hi = 0, len(nums)
        mid = lo + (hi - lo)//2
        a1 = nums[lo:mid]
        a2 = nums[mid:hi]
        a1 = self.mergeSort(a1)
        a2 = self.mergeSort(a2)
        return self.merge(a1,a2)

    def merge(self, a1,a2):
        i,j =0,0
        merged = []
        while i < len(a1) and j < len(a2):
            if a1[i] <= a2[j]:
                merged.append(a1[i])
                i += 1
            else:
                merged.append(a2[j])
                j += 1
        
        while i < len(a1):
            merged.append(a1[i])
            i += 1
        while j < len(a2):
            merged.append(a2[j])
            j += 1
        return merged



