//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.lang.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            String inputLine[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);

            int start[] = new int[n];
            int end[] = new int[n];

            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++)
                start[i] = Integer.parseInt(inputLine[i]);

            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) 
                end[i] = Integer.parseInt(inputLine[i]);
                
            int ans = new Solution().maxMeetings(start, end, n);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends

class meeting {
    private int start;
    private int end;
    private int pos;
    public meeting(int start, int end, int pos) {
        this.start = start;
        this.end = end;
        this.pos = pos;
    }
    public int getStart() { return this.start; }
    public int getEnd() { return this.end; }
    public int getPos() { return this.pos; }
    public void setStart(int start) { this.start = start; }
    public void setEnd(int end) { this.end = end; }
    public void setPos(int pos) { this.pos = pos; }
}

class comparator implements Comparator<meeting> {
    public int compare(meeting a, meeting b) {
        if(a.getEnd() == b.getEnd()) return a.getPos() - b.getPos();
        return a.getEnd() - b.getEnd();
    }
}

class Solution 
{
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    public static int maxMeetings(int start[], int end[], int n)
    {
        // add your code here
        meeting[] meetings = new meeting[n];
        for(int i = 0; i < n; i++) {
            meetings[i].setStart(start[i]);
            meetings[i].setEnd(end[i]);
            meetings[i].setPos(i + 1);
        }
        Arrays.sort(meetings, new comparator());
        int res = 1, limit = meetings[0].getEnd();
        for(int i = 1; i < n; i++) {
            if(meetings[i].getStart() > limit) {
                limit = meetings[i].getEnd();
                res++;
            }
        }
        return res;
    }
}