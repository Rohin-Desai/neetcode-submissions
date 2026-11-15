class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        general approach: Find the closest element using bin
        search
        """
        lo = 0
        hi = len(arr)
        n = len(arr)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if arr[mid] >= x:
                hi = mid
            else:
                lo = mid+ 1
        #lo is the first element greater than or equal to x. 
        l,r = lo,lo
        #r and l are both cuts between lo-1 and lo cell.
        while r - l < k :
            if l > 0 and r < n:
                if abs( arr[l-1] - x ) <= abs( arr[r] - x ):
                    #expand left
                    l -= 1
                else: # abs( arr[l-1] - x ) > abs( arr[r] - x ):
                    #expand right
                    r += 1
            elif l <= 0 and r < n:
                r += 1
            else: # l > 0 and r >=n:
                l -= 1
        return arr[l:r]
           


        