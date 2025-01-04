#User function Template for python3
class Solution:
    ans = []
    direction = [[1, 0], [-1, 0], [0, 1], [0, 1]]
    p = ['D', 'U', 'R', 'L']

    def solve(self, x: int, y: int, m: list, s: str, n: int) -> None:
        if x == n - 1 and y == n - 1:
            self.ans.append(s)
            return
        for i in range(4):
            if x + self.direction[i][0] >= 0 and x + self.direction[i][0] < n and y + self.direction[i][1] >= 0 and y + self.direction[i][1] < n and m[x + self.direction[i][0]][y + self.direction[i][1]] == 1:
                m[x][y] = 0
                self.solve(x + self.direction[i][0], y + self.direction[i][1], m, s + self.p[i], n)
                m[x][y] = 1

    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        self.ans.clear()
        if mat[0][0] == 1:
            self.solve(0, 0, mat, "", len(mat))
        return self.ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends
