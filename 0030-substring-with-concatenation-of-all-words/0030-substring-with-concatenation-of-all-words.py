class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        
        wordLength = len(words[0])
        wordsDict = {}
        for w in words:
            wordsDict[w] = wordsDict.get(w,0) + 1
        res = []
        for k in range(wordLength):
            l = k
            subd = {}
            count = 0
            for j in range(k, len(s)-wordLength+1, wordLength):
                tword = s[j:j+wordLength]
                
                if tword in wordsDict:
                    subd[tword] = subd.get(tword,0) + 1
                    count += 1
                    while subd[tword] > wordsDict[tword]:
                        subd[s[l:l+wordLength]] -= 1
                        l += wordLength
                        count -= 1
                    if count == len(words):
                        res.append(l)
                # not valid
                else:
                    l = j + wordLength
                    subd = {}
                    count = 0

        return res