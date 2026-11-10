class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1

        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j] and (j - i <= k):
                return True

            elif nums[i] != nums[j] and (j - i + 1<= k):
                j += 1

            else:
                i += 1
                j = i + 1
            
        return False
            
            