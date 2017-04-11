writer="Daniel Keyes*1927-08-15*2014-06-15"
#print(writer)
space=writer.find(' ')
#print(space)
star=writer.find('*')
#print(star)
dash=writer.find('-')
#print(dash)
name=writer[0:star]
#print(name)
dateofbirthaday=writer[star+1:dash]
#print(dateofbirthaday)
dateofdeath=writer[24:28]
#print(dateofdeath)
dateofbirthaday=int(dateofbirthaday)
dateofdeath=int(dateofdeath)
print(name,dateofdeath-dateofbirthaday)