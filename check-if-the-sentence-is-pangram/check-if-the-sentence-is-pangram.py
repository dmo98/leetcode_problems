class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Using a HashSet
        letters = set(sentence)
        if len(letters) == 26:
            return True
        else:
            return False
        