class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        8:49pm
        """
        arrSum = 0
        c = {}
        c[0] = 1
        count = 0
        for i in range(len(nums)):
            arrSum += nums[i]
            x = arrSum - k
            if x in c:
                count += c[x]
            if arrSum in c:
                c[arrSum] += 1
            else:
                c[arrSum] = 1
        return count


        