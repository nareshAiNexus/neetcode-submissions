class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        tags = {"{": "}", "[": "]", "(":")"}

        for tag in s:
            if tag in tags:
                stack.append(tag)
            else:
                if not stack:return False
                
                last_tag = stack[-1]
                if last_tag not in tags:
                    return False
                if tags[last_tag] != tag:
                    return False
                stack.pop()
        return True if not stack else False
