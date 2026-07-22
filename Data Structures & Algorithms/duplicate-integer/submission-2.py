class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fq={}
        for i in nums:
            if i not in fq:
                fq[i]=1
            else :
                return True

        return False
        