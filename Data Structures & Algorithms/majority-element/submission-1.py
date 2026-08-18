class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]
        thres = len(nums)/2
        count = {}

        for i in nums:
            count[i] = 1 if i not in count else 1 + count.get(i)
            if count[i] > thres:
                return i
        
