class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = set('aeiouAEIOU')
        list_s = list(s)
        left, right = 0, len(list_s) - 1

        while left < right:
            while left < right and list_s[left] not in vowels_set:
                left += 1

            while left < right and list_s[right] not in vowels_set:
                right -= 1

            if left < right:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                left += 1
                right -= 1

        return "".join(list_s)
