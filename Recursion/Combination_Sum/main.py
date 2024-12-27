class Solution:
    ans = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.helper(candidates, target, 0, [])
        return self.ans

    def helper(self, arr: List[int], total: int, ind: int, temp: List[int]):
        if ind == len(arr):
            return
        if arr[ind] == total:
            temp2 = []
            temp2.extend(temp)
            temp2.append(arr[ind])
            self.ans.append(temp2)
            return
        if arr[ind] > total:
            return
        self.helper(arr, total, ind + 1, temp)
        temp2 = []
        temp2.extend(temp)
        temp2.append(arr[ind])
        self.helper(arr, total - arr[ind], ind, temp2)
