from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        results = []

        for st in strs:
            sorted_st = tuple(sorted(st))
            anagram_map[sorted_st].append(st)

        for key in anagram_map.keys():
            results.append(anagram_map[key])

        return results