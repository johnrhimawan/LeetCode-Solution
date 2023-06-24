class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            sorted_string = ''.join(sorted(str))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = [str]
                continue
            hashmap[sorted_string].append(str)
        
        return list(hashmap.values())
