class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        length = len(s)
        
        for i in s:
            if i not in dict:
                stack.append(i)
            else:
                if stack == [] or stack.pop() != dict[i]:
                    return False
        
        return stack == []