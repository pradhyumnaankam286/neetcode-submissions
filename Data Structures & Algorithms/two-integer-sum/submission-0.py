class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            x = target-nums[i]
            if x not in freq:
                freq[nums[i]] = i
            else:
                return [freq[x],i]