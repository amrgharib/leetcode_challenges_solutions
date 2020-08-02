class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper():
            # All capital
            if word[1:].isupper():
                return True

            # Capital first letter
            elif word[1:].islower():
                return True

        # All small
        elif word[1:].islower():
            return True

        return False