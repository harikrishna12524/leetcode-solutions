class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = {}

        for string in strs:
            b = list(string)
            b.sort()
            sortedstr = "".join(b)
            if sortedstr not in wordmap:
                wordmap[sortedstr] = []
            wordmap[sortedstr].append(string)

        return list(wordmap.values())