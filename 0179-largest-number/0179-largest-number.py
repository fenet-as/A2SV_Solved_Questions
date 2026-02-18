class Solution:
    def largestNumber(self, arr: List[int]) -> str:

        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                fh = str(arr[j])
                sh = str(arr[j+1])
                if sh + fh  > fh + sh:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

        if arr[0] == 0:
            return "0"
        for i in range(len(arr)):
            arr[i] = str(arr[i])
 
        
        return ''.join(arr)
                
            