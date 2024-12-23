class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

#User function Template for python3
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        items = []
        for i in range(len(val)):
            items.append(Item(val[i], wt[i]))
        items.sort(key=lambda x: x.value / x.weight, reverse=True)
        cur_weight, res = 0, 0.0
        for i in range(len(items)):
            if cur_weight + items[i].weight <= capacity:
                cur_weight += items[i].weight
                res += items[i].value
            else:
                remain = capacity - cur_weight
                res += items[i].value / items[i].weight * remain
                break
        return res

#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends
