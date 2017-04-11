my_srting='Smow must start'
#print(my_srting)
space=my_srting.find(' ')
#print(space)
secondspace=my_srting.rfind(' ')
#print(secondspace)
second=(my_srting[space:secondspace])
#print(seond)
first=my_srting[0:space]
fird=my_srting[secondspace::]
#print(first)
#print(fird)
print(first,second.upper(),fird)
