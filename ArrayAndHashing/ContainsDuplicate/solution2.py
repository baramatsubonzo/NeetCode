class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == num[i - ]:
                return True
            return False
