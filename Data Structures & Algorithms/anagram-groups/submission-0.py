class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        l=[]
        seen=set()
        for i in strs:
            a=''.join(sorted(i))
            if a not in freq:
                freq[a]=[i]
            else:
                freq[a].append(i)
        for i in freq.values():
            l.append(i)
        return l