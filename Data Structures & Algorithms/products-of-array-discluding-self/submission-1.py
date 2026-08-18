class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res = []
        prefix = [1]
        suffix = [[] for _ in range(len(nums))]
        suffix[-1] = 1

        for i in range(len(nums) - 1):
            total = nums[i] * prefix[i]
            prefix.append(total)
        
        for j in range(len(nums) - 1, 0, -1):
            total = nums[j] * suffix[j]
            suffix[j-1] = total
        
        for n in range(len(nums)):
            res.append(prefix[n] * suffix[n])
        
        return res

                                                                                                         