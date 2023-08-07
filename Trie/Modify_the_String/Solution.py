# Problem: Modify the String
# Problem Statement: Given a string input_str of length n, choose any character that occurs atleast twice and delete any one occurence. Repeat this until all remaining characters are distinct. Return the lexicographically maximum string that can be formed this way.
# Example: input_str = "aabcb"
# The length of the string, n = 5. Some of the strings that can be formed are:
#     "acb" - delete the first occurences of 'a' and 'b'
#     "abc" - delete the first occurence of 'a' and the second occurence of 'b'
# It can be proven that the lexicographically maximum string that can be obtained is "acb"

class Trie:
    words = []
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