class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_hash = {}

        for i, v in enumerate(nums):
            if v in empty_hash:
                return [empty_hash[v], i]
            else:
                difference = target - v
                empty_hash[difference] = i

