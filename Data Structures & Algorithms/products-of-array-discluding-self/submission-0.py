class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1]  * (N)

        pre = 1
        for i in range(N):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(N-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        print(res)
        return res