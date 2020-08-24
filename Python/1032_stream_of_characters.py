class Trie:
    def __init__(self):
        self.end_of_word = False
        self.children = [None]*26
    
    def insert(self, s):
        tr = self
        
        for c in s:
            if tr.children[ord(c)-ord('a')] == None:
                tr.children[ord(c)- ord('a')] = Trie()
            tr = tr.children[ord(c)-ord('a')]
        
        tr.end_of_word = True
    
    def search(self, s):
        tr = self
        
        for c in s:
            if tr.children[ord(c)-ord('a')] == None:
                return False
            tr = tr.children[ord(c)-ord('a')]
            if tr.end_of_word:
                return True
        
        return False
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.tr = Trie()
        self.stream = deque()
        
        for w in words:
            self.tr.insert(reversed(w))
            
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.tr.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)




# Top solution
#class StreamChecker:
#
#    def __init__(self, words: List[str]):
#        self.trie, self.q = {}, deque()
#        
#        for word in set(words):
#            node = self.trie
#            
#            for ch in word[::-1]:
#                if ch not in node:
#                    node[ch] = {}
#                node = node[ch]
#            node['$'] = {}
#        
#
#    def query(self, letter: str) -> bool:
#        self.q.appendleft(letter)
#        
#        node = self.trie
#        
#        for ch in self.q:
#            if '$' in node:
#                return True
#            
#            if ch not in node:
#                return False
#            node = node[ch]
#        return '$' in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
