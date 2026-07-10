class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        sorted_dict = dict(sorted(freqMap.items(), key=lambda x: x[1], reverse=True))

        final = []

        for key in list(sorted_dict)[:k]:
            final.append(key)

        return final


