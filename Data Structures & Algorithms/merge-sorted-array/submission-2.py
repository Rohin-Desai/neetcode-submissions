class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #below are fences
        i = n #at the end sorted nums in nums2
        #everything between i and m is put in place in nums2
        j = m #at the end of nums1 array
        #everything to the right of j is put in place already in nums1
        k = m + n #at the end of nums1 array
        #everything to the right of k, is merged and ordered
        while j > 0 and i > 0:
            if nums1[j-1] >= nums2[i-1]:
                nums1[k-1] = nums1[j-1]
                k -= 1
                j -= 1
            elif nums1[j-1] < nums2[i-1]:
                nums1[k-1] = nums2[i-1]
                k -= 1
                i -= 1
        while i > 0:
            nums1[k-1] = nums2[i-1]
            k -= 1
            i -= 1
        while j > 0:
            nums1[k-1] = nums1[j-1]
            k -= 1
            j -= 1
        print("i " + str(i))
        print("j " + str(j))
        print("k " + str(k))

      
                    

        