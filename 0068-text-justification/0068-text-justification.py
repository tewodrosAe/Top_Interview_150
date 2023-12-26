class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current, length = [], 0
        
        for i in range(len(words)):
            if length + len(current) + len(words[i]) > maxWidth:
                space = (maxWidth - length) // max(1,len(current)-1)
                extra = (maxWidth - length) % max(1,len(current)-1)
                
                for j in range(max(1,len(current) - 1)):
                    current[j] += " " * space
                    if extra:
                        current[j] += " "
                        extra -= 1
                res.append("".join(current))
                current, length = [],0
            current.append(words[i])
            length += len(words[i])
            i += 1
        res.append(" ".join(current) + " " * (maxWidth - length - (len(current)- 1)))
        return res
        