#selection sort - Assending order

list1=[]
temp=0
num=int(input("Enter ur list size = "))
print("Enter list values")
for j in range(num):
    list1.append(int(input()))
#print(list1)
for i in range(len(list1)-1):
    for k in range(i+1,len(list1)):
        if(list1[i]>list1[k]):
            temp=list1[i]
            list1[i]=list1[k]
            list1[k]=temp
print("Selection sorted list = ",list1)
