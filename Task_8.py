First_string="in our galaxy infinity types of diferent planets"
Second_string="London is the capital of United Kingdom"
#print(len(First_string))
#print(len(Second_string))
x=Second_string[:len(Second_string)//2]
#print(x)
y=(Second_string[len(Second_string)//2:])
#print(y)
print("Result of 'first in second'"),print(x+First_string+y)
c=First_string[:len(First_string)//2]
#print(c)
d=(First_string[len(First_string)//2:])
#print(d)
print("Last result"),print(c+(x+First_string+y)+d)