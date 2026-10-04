class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'(' : ')', '[': ']', '{': '}'}
        for b in s:
            if b in matches:
                stack.append(b)
            else:
                if not stack:
                    return False
                if matches[stack.pop()] == b:
                    continue
                return False
        return not stack
                