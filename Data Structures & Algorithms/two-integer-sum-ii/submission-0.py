class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        solution DRD on 10/18/2026
        two pointer lo, hi. 
        while lo < hi so they are never equal
        """
        lo = 0
        hi = len(numbers) - 1
        returnValue = None
        while lo < hi:
            n = numbers[lo] + numbers[hi]
            if n == target:
                returnValue = [lo+1,hi+1]
            if n < target:
                lo += 1
            else:
                hi -= 1
        return returnValue #As stated there will always be a return value
        