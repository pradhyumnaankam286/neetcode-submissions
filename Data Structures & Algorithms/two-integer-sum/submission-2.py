class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x  not in ind:
                ind[nums[i]]=i
            else:
                return[ind[x],i]
                
        
        