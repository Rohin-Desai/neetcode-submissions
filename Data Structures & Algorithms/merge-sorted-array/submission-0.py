class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        7:47pm
        """
        buffer = [0] * m
        k = 0 #for nums1 where we will copy all elements
        i = 0 #for for buffer where we copied first m of nums1
        j = 0 #for nums2
        for z in range(m):
            buffer[z] = nums1[z] #After this nums1 becomes the place where we copy everything. 
        while i < m and j < n :
            if buffer[i] <= nums2[j]:
                nums1[k] = buffer[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
        while i < m:
            nums1[k] = buffer[i]
            k += 1
            i += 1
        while j < n:
            nums1[k] = nums2[j]
            k += 1
            j += 1


        