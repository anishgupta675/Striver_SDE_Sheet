#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i, j, last_element = 0, 0, min(a[0], b[0])
        while i < len(a) and j < len(b):
            if not k:
                return last_element
            if a[i] <= b[j]:
                last_element = a[i]
                i += 1
            else:
                last_element = b[j]
                j += 1
            k -= 1
        if i < len(a):
            return a[i + k - 1]
        if j < len(b):
            return b[j + k - 1]
        return -1
