class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        10:47am
        0 red, 1 white, 2 blue
        """
        n = len(nums)
        i,j,k = 0,0,n
        while j < k: #between fences j and k is the unprocessed
            if nums[j] == 0: #red
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # move j past the red so the red is now left of j
                i += 1 #the red is now to the left of i
            elif nums[j] == 1: #White
                j += 1 #move past the white, so this white is to the left of the fence j (and between i and j)
            else: #nums[j] == 2, blue
                nums[j], nums[k-1] = nums[k-1], nums[j]
                #remember we think of k as a fence and the unprocessed cell is to the
                #left of k.
                k -= 1 #Now the blue is to the right of the k fence
                #We don't increment j fence since we don't know yet what is to immiediately to the right of it (we'll find out next iteration)






        