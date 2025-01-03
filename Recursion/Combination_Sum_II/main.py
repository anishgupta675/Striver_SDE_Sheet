class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List < List < Integer >> result = new ArrayList();
        find(result, candidates, target, 0, new ArrayList < Integer > ());
        return result;
    }
    public void find(List < List < Integer >> result, int[] candidates, int target, int from, List < Integer > list) {
        if (target == 0) {
            result.add(new ArrayList < Integer > (list));
        } else if (target > 0) {
            for (int i = from; i < candidates.length && candidates[i] <= target; i++) {
                if (i > from && candidates[i] == candidates[i - 1]) continue;
                list.add(candidates[i]);
                find(result, candidates, target - candidates[i], i + 1, list);
                list.remove(list.size() - 1);
            }
        }
    }
}
