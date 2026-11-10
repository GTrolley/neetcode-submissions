class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = set()

        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            
            hs.add(nums[i])

            if len(hs) > k:
                hs.remove(nums[i-k])
            
        return False
            
            