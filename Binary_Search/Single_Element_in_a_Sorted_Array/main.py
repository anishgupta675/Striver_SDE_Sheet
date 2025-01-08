class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] == nums[mid + 1]:
                mid -= 1
            if (mid - l + 1) % 2:
                r = mid
            else:
                l = mid + 1
        return nums[l]
