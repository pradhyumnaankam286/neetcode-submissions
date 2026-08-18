class Solution:
    def isPalindrome(self, s1: str) -> bool:
        s=s1.lower()
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True