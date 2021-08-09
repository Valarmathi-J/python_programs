#reversearray
n = int(input())
arr=[]
li=[]
for i in range(0,n):
    arr.append(int(input()))
    

#print(arr)
for i in range(len(arr)):
    print(arr[len(arr)-i-1],end="")
