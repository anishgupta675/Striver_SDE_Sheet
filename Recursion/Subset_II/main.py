class Solution:
    def sub(self, index: int, arr: List[int], ans: List[int], li: List[int]):
        ans.append([li])
        for i in range(index, len(arr)):
            if i > index and arr[i] == arr[i - 1]:
                continue
            li.append(arr[i])
            self.sub(i + 1, arr, ans, li)
            li.pop(len(li) - 1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.sub(0, nums, ans, [])
        return ans
