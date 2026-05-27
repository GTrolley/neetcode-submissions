class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = []

        for i in nums:
            if i in appeared:
                return True
            else:
                appeared.append(i)
        
        return False
        
        