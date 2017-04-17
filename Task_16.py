v_1=60
v_2=55
def time(v_1,v_2):
   time_1=10/(v_1+v_2)
   time_2=4/v_1
   if time_2<time_1:
       print('Not boom!')
   else:
       print("Boom:(")
result=time(v_1,v_2)
#print(time(v_1,v_2))
print( "In case V of first train %d and V of second train %d"% (v_1,v_2))