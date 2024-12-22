#User function Template for python3

class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    # Function used for sorting jobs according to their deadlines
    def JobSequencing(self, id, deadline, profit):
        #code here
        jobs = []
        for i in range(len(id)):
            jobs.append(job(id[i], deadline[i], profit[i]))
        count, max_profit = 0, 0
        done = [0] * len(jobs)
        jobs.sort(key=lambda x: x.profit, reverse=True)
        for i in range(len(jobs)):
            for j in range(min(len(jobs), jobs[i].deadline - 1), -1, -1):
                if not done[j]:
                    count += 1
                    max_profit += jobs[i].profit
                    done[j] = 1
                    break
        return [count, max_profit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        job_ids = list(map(int, input().split()))
        deadlines = list(map(int, input().split()))
        profits = list(map(int, input().split()))
        obj = Solution()
        ans = obj.JobSequencing(job_ids, deadlines, profits)
        print(ans[0], ans[1])
        print("~")

# } Driver Code Ends
