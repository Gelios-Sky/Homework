writer="Daniel Keyes*1927-08-15*2014-06-15"
#print(writer)
space=writer.find(' ')
#print(space)
star=writer.find('*')
#print(star)
second_star=writer.rfind('*')
#print(second_star)
second_dash=writer.rfind('-')
print(second_dash)
dash=writer.find('-')
#print(dash)
name=writer[0:star]
#print(name)
dateofbirthaday=writer[star+1:dash]
#print(dateofbirthaday)
dateofdeath=writer[second_star+1:second_dash-3]
print(dateofdeath)
dateofbirthaday=int(dateofbirthaday)
dateofdeath=int(dateofdeath)
print(name,dateofdeath-dateofbirthaday)