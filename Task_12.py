def formula(number):
    numeral_1=number%10
    numeral_2=number%100//10
    numeral_3=number//100
    result=numeral_1+numeral_2+numeral_3
    return result
#print(formula(454))
number=int(input('Enter your number'))