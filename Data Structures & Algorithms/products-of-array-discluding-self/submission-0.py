class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[]
        final=[]
        for i in range(len(nums)):
            p=nums.copy()
            p[i]=1
            t=1
            for j in p:
                t*=j
            final.append(t)
        return final