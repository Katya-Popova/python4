#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n= int(input())
z= 2 # первый простой множетель
some_list=[]
while z<=n:
    if n%z==0:
        some_list.append(z)
        n=n/z
    else:
        z+=1
print(some_list)
