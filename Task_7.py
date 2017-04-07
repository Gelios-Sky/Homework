date_am=("04.07.2017")
#(date_am.split('.'))
#dot=date_am.find('.')
#days=date_am[0:dot]
#mounths=date_am[dot+2]
#print(mounths)
days=date_am[3:6]
#print(days)
mounths=date_am[0:3]
#print(mounths)
years=date_am[6:10]
#print(years)
date_eu=(days+mounths+years)
print("Change date tipe from Am to Eu"),print(date_eu)