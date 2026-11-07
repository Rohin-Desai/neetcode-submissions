class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        there are 2n+1 positions
        0 is the fencecut before cell 0. 
        0 fenecut, 1 is cell n-1 is cell, n is fencecut
        2 is fencecut between cell 1 and 3
        even is fencecut, odd is cell
        """
        i = 0
        n = len(s)
        longestPalindrome = ""
        while i <= 2*n: #iterate over fencecuts.
            j,k = i,i #assume i even
            if i % 2 != 0: #means i is pointing at cell
                j,k = i - 1, i + 1  #we note that j and k are always even.
            while j >= 0 and k <= 2*n :
                #_j = ((j+1) - 1)//2 #cell to right of j
                _j = j//2
                _k = (k-1)//2
                #_k = ((k-1) - 1)//2 #cell to left of k
                if (_j < 0 or _j >= n or _k < 0 or _k >= n) or s[_j] != s[_k]:
                    break #It's not a palindrome
                l = (k - j)//2
                if len(longestPalindrome) < l:
                    #longestPalindrome = s[_j:_k + 1]
                    longestPalindrome = s[_j:_j + l]
                j -= 2
                k += 2                
            i += 1
        return longestPalindrome




