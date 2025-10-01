class Solution:
    p_mapping = {"(": ")", "{": "}", "[": "]"}
    inverse_p_mapping = {v: k for k, v in p_mapping.items()}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.p_mapping:
                # opening
                stack.append(c)
            else:
                # closing
                expected_opening = self.inverse_p_mapping[c]
                try:
                    if expected_opening != stack.pop():
                        return False
                except IndexError:
                    return False
        return len(stack) == 0