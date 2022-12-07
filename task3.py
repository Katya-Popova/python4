#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
some_list=list(map(int,input().split()))
new_list=[]
for i in range(len(some_list)):
    if some_list.count(i)==1:
        new_list.append(i)
print(new_list)