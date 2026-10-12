class Solution:
    def largest(self, arr):
        # code here
        largest01 = float('-inf')
        for i in range (0, len(arr)):
            if largest01 < arr[i]:
                largest01 = arr[i]
                
        return largest01     
