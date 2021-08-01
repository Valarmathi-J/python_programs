#Bubble sort

bub_list=[]
temp=0
num=int(input("Enter ur list size = "))
print("Enter list values")
for i in range(num):
    bub_list.append(int(input()))

for j in range(len(bub_list)-1):
    for k in range(len(bub_list)-1):
        if(bub_list[k]>bub_list[k+1]): 
            temp=bub_list[k]
            bub_list[k]=bub_list[k+1]
            bub_list[k+1]=temp
print("Bubble sorted list = ",bub_list)
