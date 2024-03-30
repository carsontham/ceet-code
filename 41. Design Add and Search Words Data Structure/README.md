# Qns : Design Add and Search Words Data Structure 
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Approach
1) Similar to implement Trie. Only difference is the search part, as now we have the wildcard ".".
2) Thus, a DFS is required.

# Solution:
```
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root

            for index in range(j, len(word)):
                char = word[index]
                
                if char == ".":
                    for child in cur.children.values():
                        if dfs(index+1, child):
                            return True
                    return False
                
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.isEndOfWord  
        return dfs(0, self.root)                     
```
---

# Time Complexity
Time complexity is O(n), worst case is all characters exist.

# Space Complexity
Space complexity is O(n), have to store n nodes.