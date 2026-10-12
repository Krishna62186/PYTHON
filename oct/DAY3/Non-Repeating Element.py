class Solution:
    def firstNonRepeating(self, arr):
        mp = {}

        for i in range(0, len(arr)):
            mp[arr[i]] = mp.get(arr[i], 0) + 1

        for i in range(0, len(arr)):
            if mp[arr[i]] == 1:
                return arr[i]

        return 0
