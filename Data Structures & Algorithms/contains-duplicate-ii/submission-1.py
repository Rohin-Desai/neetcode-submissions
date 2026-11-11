class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        sliding window of size k.   
        hash the values in dict with count as to num appearances
        When you slide the window, remove the num on the left (or decrement the count)
        and add the new element that scrolls into view. 
        If any count is ever greater than 1, then return true
        assume k <= n
        """
        d = {} #Could just use set instead of dict. 
        #initialize
        for i in range(min(k+1, len(nums))): #0 to k-1
            n = nums[i]
            if n in d:
                return True
            else:
                d[n] = 1
        #Now slide the window
        j = k+1 #just to the right of the first window.
        while j < len(nums):
            lef = j - (k + 1)
            if nums[lef] in d:
                d.pop(nums[lef])
            if nums[j] in d:
                return True
            else:
                d[nums[j]] = 1
            j += 1
        return False


        