class Solution:
    def noofvowelinsubstrng(self, s:str, queries:list ) -> int:
        n = len(s)
        prefix = [0]*(n+1)
        vowel ="aeiouAEIOU"

        for i in range(n):
            prefix[i+1] = prefix[i] + [1 if s[i] in vowel else 0]

        result = []

        for l, r in queries:
            result.append(prefix[r+1] - prefix[l])

        return result
