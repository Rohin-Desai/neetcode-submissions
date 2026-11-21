class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        i = 0
        for j in range(1,len(nums) + 1):
            if j - i > k + 1 :
                seen.remove(nums[i])
                i += 1
            if nums[j - 1] in seen: return True
            seen.add(nums[j-1])
        return False
