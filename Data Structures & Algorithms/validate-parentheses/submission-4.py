class Solution:
    def isValid(self, s: str) -> bool:
        closingTags = {')':'(', '}':'{', ']':'['}
        stack = []
        for tag in s:
            if tag in closingTags:
                if stack and stack[-1] == closingTags[tag]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(tag)
        return not stack