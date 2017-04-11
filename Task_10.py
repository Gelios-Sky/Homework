writer="Daniel Keyes*1927-08-15*2014-06-15"
#print(writer)
space=writer.find(' ')
#print(space)
star=writer.find('*')
#print(star)
second_star=writer.rfind('*',star+1)
#print(second_star)
second_dash=writer.rfind('-',second_star)
#print(second_dash)
dash=writer.find('-')
#print(dash)
name=writer[0:star]
#print(name)
date_of_birthaday=writer[star+1:dash]
#print(dateofbirthaday)
date_of_death=writer[second_star+1:second_dash-3]
#print(date_of_death)
date_of_birthaday=int(date_of_birthaday)
date_of_death=int(date_of_death)
print(name,date_of_death-date_of_birthaday)