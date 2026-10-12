class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = float('-inf')
        for i in range(0, len(arr)):
            if largest < arr[i]:
                largest = arr[i]
                
                
        secondlargest = float('-inf') 
        for i in range (0 , len(arr)):
            if secondlargest < arr[i] and arr[i] != largest:
                secondlargest = arr[i]
                
        if secondlargest == float('-inf'):
                   return -1        
        return secondlargest        