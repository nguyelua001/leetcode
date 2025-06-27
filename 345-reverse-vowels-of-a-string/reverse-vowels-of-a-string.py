class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set for efficient vowel lookup
        s = list(s)  # Convert to list for mutability
        left, right = 0, len(s) - 1  # Initialize pointers

        while left < right:  # Loop until pointers cross
            # Move left pointer until a vowel is found
            while left < right and s[left] not in vowels:
                    left += 1

            # Move right pointer until a vowel is found
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap vowels if both pointers are on vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)  # Convert list back to string