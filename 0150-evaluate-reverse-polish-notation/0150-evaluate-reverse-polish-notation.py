class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # iterate through the array and put the numbers in the stack
        # whenever we find a calc we calc the last two from our stack
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            elif t == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            else:
                stack.append(int(t))
        return stack[0]