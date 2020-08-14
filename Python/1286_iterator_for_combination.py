class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = []
        
        def gen_combs(st, l, pcomb):
            if l == 0:
                self.combs.append(pcomb)
                return
            for i in range(st, len(characters) - l + 1):
                gen_combs(i+1, l-1, pcomb + characters[i])
                
        gen_combs(0, combinationLength, "")
        

    def next(self) -> str:
        return self.combs.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.combs) > 0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
