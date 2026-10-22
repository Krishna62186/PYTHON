class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        res = arr[:k]
        return res
        
        # Code here
        
