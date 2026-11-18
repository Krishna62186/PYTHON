class Solution:
    def sortbyfrequency(self, s: str) -> str:
        freq = {}
        for k in s:
            if k not in freq:
                freq[k] = 1
            else:
                freq[k] += 1

        chars = list(freq.keys())

        for i in range (len(chars)):
            largest = i
            for j in range(i+1, len(chars)):
                if freq[chars[j]] > freq[chars[largest]]:
                    largest = j
            chars[i], chars[largest] = chars[largest], chars[i]

        res = ""
        for i in chars:
            res += i*freq[i]

        return res
