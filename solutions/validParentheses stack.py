class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        stack = []
        
        for p in s:
            if p in open:
                stack.append(p)
            elif p in close:
                index = close.index(p)
                if (len(stack) > 0) and (stack[-1] == open[index]):
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
        
                
                
        