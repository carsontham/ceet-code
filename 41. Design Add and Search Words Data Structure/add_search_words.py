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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)