class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref,suff=1,1
        maxp=float('-inf')
        for i in range(len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[len(nums)-i-1]
            maxp=max(maxp,max(pref,suff))

        return maxp
        