class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        counter = 0
        i = 0

        for ele in nums:
            if ele != val:
                nums[i] = ele
                counter += 1
                i += 1 


       

        return counter 




