class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Could use heaps, but for now try different approach
        1) use Dictionary for frequency count
        2) Sort entries according to frequency
            SKILL: how do you get dictionary entries (items()) and sort according to the value? Use sorted(items, key=lambda item : item[1])
        """
        
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        sortedCounts = sorted(counts.items(), key=lambda item: item[1])
        l = len(sortedCounts)
        v = []
        for i in range(l-1, l-k-1,-1):
            v.append(sortedCounts[i][0])
        return v

