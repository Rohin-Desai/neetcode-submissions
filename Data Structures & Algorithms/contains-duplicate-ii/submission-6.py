class Solution:
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        """
        if abs(i - j) == k: assume j is the right index.
        then [i,j+1) means j+1 - i = k
        But if we want i and j to be the fences not cells so 
        [i,j) -> j - i = k + 1 where the left cell is i and the right one is j-1
        """
        ns = {}
        i = 0
        for j in range(1,len(nums) + 1) :
            if j - i > k + 1:
                self.remove(ns,nums[i])
                i += 1
            if nums[j-1] in ns: return True #incoming cell
            self.add(ns, nums[j-1])
               
        return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ns = {}
        i = 0
        for j in range(1, len(nums) + 1):
            if j - i > k + 1:
                self.remove(ns,nums[i])
                i += 1
            if nums[j-1] in ns: return True
            ns[nums[j-1]] = 1 #nums[j-1] is not in ns cause we checked above. We don't need to do self.add!!!!
            #self.add(ns, nums[j-1])
        return False




    def remove(self, d, n):
        if n in d:
            d[n] -= 1
            if d[n] == 0:
                del d[n]

    def add(self, d, n):
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
            

        