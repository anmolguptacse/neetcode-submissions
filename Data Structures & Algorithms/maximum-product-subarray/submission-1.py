class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax=1
        currMin=1
        res=0
        if len(nums)==1:
            return nums[0]
        for n in  nums:
            temp=currMax
            if n==0:
                currMax,currMin=1,1
                continue
            currMax=max(n,currMax*n,currMin*n)
            currMin=min(n,temp*n,currMin*n)
            res=max(res,currMax)
        return res


            