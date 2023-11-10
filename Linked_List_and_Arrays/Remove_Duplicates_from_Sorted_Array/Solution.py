class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 1
        count = 1
        prev = nums[0]
        while i < len(nums):
            while i < len(nums) and nums[i] == prev:
                i += 1
            if i < len(nums):
                prev = nums[i]
                nums[count] = nums[i]
                count += 1
        return count