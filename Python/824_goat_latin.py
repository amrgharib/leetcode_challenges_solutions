class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = S.split()
        goat_s = []
        
        for i, w in enumerate(l):
            if w[0].lower() in ["a","e","i","o","u"]:
                goat_s.append(w + "ma" + "a" * (i+1))
            
            else:
                goat_s.append(w[1:] + w[0] + "ma" + "a" * (i+1))
        
        
        
        return " ".join(goat_s)
