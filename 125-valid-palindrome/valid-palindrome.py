class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        list_string = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                list_string += char.lower()
        rev = "".join(reversed(list_string))
        if list_string == rev:
            return True
        
        return False