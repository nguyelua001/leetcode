class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Initialize with -1 to handle edge cases
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)  # Push the index of '('
            else:
                stack.pop()  # Pop the last unmatched '('
                if not stack:
                    stack.append(i)  # If stack is empty, push current index
                else:
                    max_len = max(max_len, i - stack[-1])  # Valid substring length

        return max_len