class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Solution by DRD. 
        Iterate over elements. Each time you hit a non val value, increment your counter
        k and move one to the right (i +=1). If you hit val, k and i stay the same but the element is not next 
        """
        i = 0
        k = 0
        """
        We stop the pointer i at the vals and the for loop goes ahead and finds
        the next num is not a val and then copies that into the 
        """
        for n in nums:
            if n != val:
                nums[i] = n
                i += 1
                k += 1
        return k
        