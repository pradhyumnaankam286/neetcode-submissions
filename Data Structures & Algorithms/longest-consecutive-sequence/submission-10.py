class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maxstreak=1
        streak=1
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                streak+=1
                # maxstreak = max(maxstreak,streak)
            elif nums[i-1]==nums[i]:
                pass
            else:
                streak=1
            maxstreak=max(maxstreak,streak)
        return maxstreak