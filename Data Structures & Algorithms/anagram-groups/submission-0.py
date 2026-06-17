class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            s_word = tuple(sorted(word))
            if s_word not in hash_map:
                hash_map[s_word] = [word]
            else:
                hash_map[s_word].append(word)
        return list(hash_map.values())
