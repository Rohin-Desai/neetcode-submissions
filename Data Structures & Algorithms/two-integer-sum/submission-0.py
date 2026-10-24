class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        solution by DRD
        use dict 
        """
        returnVal = [0,0]
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                k = d[target - n]
                returnVal  = [k,i]
                break
            if n not in d:
                d[n] = i
        return returnVal

        