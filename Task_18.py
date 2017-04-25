for i in range(65, 91):
    print(chr(i), end=' ')
    if (i - 2) % 10 == 0:
        print()

print()

total=0
sum_of_unicode= 0
input("Выберите 2 литеры алфавита(англ)")
x_1=input("Первая =")
x_2=input("Вторая =")
x_1=ord(x_1)
x_2=ord(x_2)
if x_1<=x_2:
  print("Unicode of your choice",x_1,x_2)
else:
    print("Не верная последовательность")
x_1=int(x_1)
x_2=int(x_2)
print (x_1)
print (x_2)
for i in range(x_1, x_2 + 1):
    sum_of_unicode += i
    print("Result",sum_of_unicode)
#for sum_of_unicode in range(x_1,x_2+1):
#    sum_of_unicode=sum_of_unicode+sum_of_unicode
#    print(sum_of_unicode)
#while x_1<=x_2:
    #total=x_1+1
    #print(total)

#print (type(x_1))
#print(x_1)
#print(x_2)
#for total in (x_1,x_2+1):
   # import math
    #if x_1<=x_2:
        #total=total+total
        #print(total)
        #for sum_of_unicode in (total):
            ##print(sum_of_unicode)
        #while total > 0:
            #sum_of_unicode = sum_of_unicode + total
            #print(sum_of_unicode)
    #elif x_1>x_2:
        #break
    #else:
        #print("Не верная последовательность")




