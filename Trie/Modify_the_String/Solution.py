# Problem: Modify the String
# Problem Statement: Given a string input_str of length n, choose any character that occurs atleast twice and delete any one occurence. Repeat this until all remaining characters are distinct. Return the lexicographically maximum string that can be formed this way.
# Example: input_str = "aabcb"
# The length of the string, n = 5. Some of the strings that can be formed are:
#     "acb" - delete the first occurences of 'a' and 'b'
#     "abc" - delete the first occurence of 'a' and the second occurence of 'b'
# It can be proven that the lexicographically maximum string that can be obtained is "acb"

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.word = False
# class Trie:
#     def __init__(self, words):
#         self.root = TrieNode()
#         for w in words:
#             curr = self.root
#             for c in w:
#                 if c not in curr.children:
#                     curr.children[c] = TrieNode()
#                 curr = curr.children[c]
#             curr.word = True

class Trie:
    words = {}
    flag = False
    def insert(self, word: str, idx: int):
        if not word:
            flag = True
            return
        if not self.words[word[idx] - 'a']:
            self.words[word[idx] - 'a'] = Trie()
        self.words[word[idx] - 'a'].insert(word, idx + 1)
    def contains(self, word: str, idx: int) -> bool:
        if not word:
            return True
        if idx == len(word):
            return self.flag
        if not self.words[word[idx] - 'a']:
            return False
        return self.words[word[idx] - 'a'].contains(word, idx + 1)
ans = []
freq = {}
def modifyString(word: str, idx: int):
    return
def modifyString(word: str) -> str:
    for i in word:
        freq[i]+= 1
    modifyString(word, 0)
if __name__ == '__main__':
    print(modifyString(input()))