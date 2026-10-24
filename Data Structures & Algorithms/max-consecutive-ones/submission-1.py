class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        tracker = 0
        currMax = 0

        for ele in nums:
            if ele == 1:
                tracker += 1
            if ele == 0:
                if tracker > currMax:
                    currMax = tracker
                tracker = 0 
  
        if tracker > currMax:
            currMax = tracker

        return currMax
            
            
