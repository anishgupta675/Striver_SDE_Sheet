#User function Template for python3

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        meet = [meeting(start[i], end[i], i + 1) for i in range(len(start))]
        sorted(meet, key=lambda x: (x.end, x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1, len(start)):
            limit = meet[i].end
            answer.append(meet[i].pos)
        return (len(answer) // 2) + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(start, end))
        print("~")

# } Driver Code Ends
