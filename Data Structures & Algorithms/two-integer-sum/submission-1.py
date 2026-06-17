class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashSet = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hashSet:
                return [hashSet[diff], idx]
            hashSet[num] = idx
        