x_1=int(input("Введите координаты x для первой окружности"))
y_1=int(input('Введите координаты y для первой окружности'))
x_2=int(input('Введите координаты x для второй окружности'))
y_2=int(input('Введите координаты y для второй окружности'))
r_1=int(input('Укажите радиус первой окружности'))
r_2=int(input('Укажите радиус второй окружности'))
def circle_in_circle(x_1,y_1,x_2,y_2,r_1,r_2):
    d=(x_1-x_2)*2+(y_1-y_2)*2
    d_1=d//2
    if d_1<=r_1+r_2:
        print("Пересекаются")
    elif [r_1-r_2]>d_1:
        print ("окружности  не пересекаются, т.к. одна окружность находится внутри другой.")
    else:
         print("Не пересекаются")
print(circle_in_circle(x_1,y_1,x_2,y_2,r_1,r_2))
