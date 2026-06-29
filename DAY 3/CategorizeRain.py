rain_detect = int(input("enter the mm of rain :"))
if rain_detect <= 1 :
    print( " No Rain ");
elif rain_detect <= 5 and  rain_detect > 1:
    print(" Light Rain ");
elif rain_detect > 5 and rain_detect <=10 :
    print(" Moderate Rain ");
else :
    print (" Heavy Rain ")

