class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_index = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_index = max(max_index, count)
        return max_index
