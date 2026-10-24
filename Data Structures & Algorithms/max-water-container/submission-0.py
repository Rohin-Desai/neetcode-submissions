class Solution:
    """
    11:53am
    """
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)  - 1
        h = heights
        maxV = -1
        while (i < j):
            v = 0
            if h[i] < h[j]:
                v = (j - i) * h[i]
                i += 1
            elif h[i] > h[j]:
                v = (j - i) * h[j]
                j -= 1
            else: #They are equal
                v = (j - i) * h[i]
                i += 1
                j -= 1
            if v > maxV: 
                maxV = v
        return maxV
