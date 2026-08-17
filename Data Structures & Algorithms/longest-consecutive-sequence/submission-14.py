class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=set(nums)
        streak=1
        maxstreak=1
        for i in nums:
            if i-1 not in nums:
                streak=1
                j=i
                while True:
                    if j+1 not in nums:
                        maxstreak=max(maxstreak,streak)
                        break
                    else:
                        streak+=1
                        j+=1
            # if i+1 in nums:
            #     streak+=1
            #     maxstreak=max(maxstreak,streak)
            #     # j+=1
            # else:
            #     streak=1
        return maxstreak



        # if not nums:
        #     return 0
        # nums.sort()
        # maxstreak=1
        # streak=1
        # for i in range(1,len(nums)):
        #     if nums[i-1]+1 == nums[i]:
        #         streak+=1
        #         # maxstreak = max(maxstreak,streak)
        #     elif nums[i-1]==nums[i]:
        #         pass
        #     else:
        #         streak=1
        #     maxstreak=max(maxstreak,streak)
        # return maxstreak