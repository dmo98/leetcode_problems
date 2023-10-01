class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reverse_words = []
        for word in words:
            characters = []
            for i in range(len(word)-1, -1, -1):
                characters.append(word[i])

            reverse_words.append("".join(characters))
        
        return " ".join(reverse_words)
        