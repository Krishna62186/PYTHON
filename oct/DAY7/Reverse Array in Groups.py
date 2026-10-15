class Solution:
    def reverseInGroups(self, arr, k):
        for i in range(0, len(arr), k):
            left = i
            right = min(i + k - 1, len(arr) - 1)

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
