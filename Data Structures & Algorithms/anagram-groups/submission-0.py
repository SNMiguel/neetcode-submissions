class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            if "".join(sorted(word)) not in seen:
                seen["".join(sorted(word))] = [word]
            else:
                seen["".join(sorted(word))].append(word)
        
        return list(seen.values())