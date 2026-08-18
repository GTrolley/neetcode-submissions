class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        match = {
            ')':'(',
            '}': '{',
            ']': '['
        }
        stack = []
        for p in s:
            if p in ['(', '{', '[']:
                stack.append(p)

            else:
                if len(stack) > 0 and stack[len(stack) - 1] == match.get(p):
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True

        return False