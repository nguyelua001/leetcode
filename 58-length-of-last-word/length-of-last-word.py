class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string = s[::-1]

        return (len(new_string.split()[0]))
        

        