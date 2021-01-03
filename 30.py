class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordnum = len(words)
        wordlenth = len(words[0])
        words = sorted(words)
        ans = list()

        def issub(string):
            # print(string)
            tmp = list()
            for i in range(0, len(string), wordlenth):
                tmp.append(string[i:i + wordlenth])
            tmp = sorted(tmp)
            if tmp == words:
                return True
            else:
                return False

        for i in range(len(s) - wordnum * wordlenth + 1):
            if issub(s[i:i + (wordnum * wordlenth)]) == True:
                ans.append(i)
        return ans