class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            for j, w in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or word[j] != words[j][i]:
                    return False

        return True



        