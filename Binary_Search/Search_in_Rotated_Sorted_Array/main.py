class Solution:
    def searchUtil(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) >> 1
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if target >= nums[low] and target <= nums[mid]:
                return self.searchUtil(nums, low, mid - 1, target)
            return self.searchUtil(nums, mid + 1, high, target)
        if target >= nums[mid] and target <= nums[high]:
            return self.searchUtil(nums, mid + 1, high, target)
        return self.searchUtil(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.searchUtil(nums, 0, len(nums) - 1, target)
