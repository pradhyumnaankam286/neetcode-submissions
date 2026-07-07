class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            a=''.join(sorted(i))
            if a not in freq:
                freq[a]=[i]
            else:
                freq[a].append(i)
        
        return list(freq.values())