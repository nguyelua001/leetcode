class Solution:
    def isValid(self, word: str) -> bool:
        # Check minimum length
        if len(word) < 3:
            return False

        # Check all characters are alphanumeric (digits or letters)
        if not word.isalnum():
            return False

        # Define vowels and consonants
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

        # Flags for vowel and consonant presence
        has_vowel = any(char in vowels for char in word)
        has_consonant = any(char in consonants for char in word)

        return has_vowel and has_consonant