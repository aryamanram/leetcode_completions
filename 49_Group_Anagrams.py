class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for word in strs:
            sortedKey = "".join(sorted(word))
            anaMap[sortedKey].append(word)
            
        return list(anaMap.values())