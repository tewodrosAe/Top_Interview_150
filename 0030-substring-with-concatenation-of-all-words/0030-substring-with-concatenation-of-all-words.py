class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLength = len(words[0])
        concatLength = len(words[0]) * len(words)
        wordsDict = {}
        res = []
        
        for word in words:
            wordsDict[word] = wordsDict.get(word,0) + 1
    
        for l in range(len(s) - concatLength + 1):
            wordsSeen = {}
            
            for r in range(l, l + concatLength, wordLength):
                tempWord = s[r: r + wordLength]
                if tempWord not in wordsDict:
                    l = r + wordLength
                    break
                wordsSeen[tempWord] = wordsSeen.get(tempWord,0) + 1
                if wordsSeen[tempWord] > wordsDict[tempWord]:
                    break
            
            if wordsSeen == wordsDict:
                res.append(l)
            
        return res