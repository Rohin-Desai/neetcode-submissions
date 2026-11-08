class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        6:14pm
        """
        i = 0
        n = len(s)
        longestPal = ""
        for i in range(2*n + 1) : #so 2n + 1 possible values starting from 0
            j,k = i,i #assuming even i. j and k are fencecuts
            if i % 2 != 0:
                j,k = i-1,i+1
            while j >= 0 and k <= 2*n :
                _j = j//2 #cell index
                _k = k//2 - 1 #cell index just to left of point. 
                l = (k - j)//2
                if ( _j < 0 or _k < 0 or _j >= n or _k >= n ) or s[_k] != s[_j]:
                    #Not palindrome
                    break
                else:
                    if l > len(longestPal) :
                        longestPal = s[j//2:k//2]
                j -= 2
                k += 2
        return longestPal

