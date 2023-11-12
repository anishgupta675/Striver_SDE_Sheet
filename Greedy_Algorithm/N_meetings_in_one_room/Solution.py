#User function Template for python3

class meeting:
    start = 0
    end = 0
    pos = 0
    def __init__(self, start: int, end: int, pos: int):
        self.start = start
        self.end = end
        self.pos = pos
    def getStart(self) -> int:
        return self.start
    def getEnd(self) -> int:
        return self.end
    def getPos(self) -> int:
        return self.pos
    def setStart(self, start) -> int:
        self.start = start
    def setEnd(self, end) -> int:
        self.end = end
    def setPos(self, pos) -> int:
        self.pos = pos

class Solution:
    
    def compare(a: meeting, b: meeting) -> int:
        if a.getEnd() == b.getEnd():
            return a.getPos() - b.getPos()
        return a.getEnd() - b.getEnd()
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = []
        for i in range(n):
            meetings.append(meeting(start[i], end[i], i + 1))
        sorted(meetings, key=cmp_to_key(compare))
        res = 1
        limit = meetings[0].getEnd()
        for i in range(1, n):
            if meetings[0].getStart() > limit:
                limit = meetings[0].getEnd()
                res += 1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends