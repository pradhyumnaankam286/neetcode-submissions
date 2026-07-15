class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        l=[]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in range(k):
            m=n=0
            for key,v in freq.items():
                if v > m:
                    m = v
                    n = key
            l.append(n)
            freq[n] = 0
        return l