class Solution: 
    def selectionSort(self, arr):
        # code here
        for i in range(0 , len(arr)-1):
            mini = i
            for j in range(i+1 , len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i] , arr[mini] = arr[mini] , arr[i]        
