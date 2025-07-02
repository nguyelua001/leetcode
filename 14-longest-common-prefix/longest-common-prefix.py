class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        common_prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
            if not common_prefix:
                return ""

        return common_prefix


