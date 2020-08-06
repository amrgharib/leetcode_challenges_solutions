import collections
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        self.word_set = set()

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
            self.word_set.add(word)

    def search(self, word):
        if word in self.word_set:
            return True
        else:
            for w in self.word_dict[len(word)]:
                for ind, char in enumerate(word):
                    if char != w[ind] and char != '.':
                        break
                else:
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)