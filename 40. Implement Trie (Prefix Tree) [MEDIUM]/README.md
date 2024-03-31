# Qns : Implement Trie https://leetcode.com/problems/implement-trie-prefix-tree/

# Approach
1) First unds how Trie works. Basically, each node has a dictionary of characters.
2) For insert(), we insert character as keys into the dict, value will be a new TrieNode(). Iterate through the entire word. After the loop, mark the last character as isEndOfWord = True
3) For search(), we are searching if that specific word exist. Iterate through the nodes, if end of word but isEndOfWord is False, this means that the prefix exist but it's not a word. Thus return false.
4) For startsWith(), similar to search(). At end of loop, return True since all char can be found.
5) pretty cool and simple implementation of Trie :D

# Solution:
```
    class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord            
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True     
               
```
---

# Time Complexity
Time complexity is O(n), worst case is all characters exist.

# Space Complexity
Space complexity is O(n), have to store n nodes.