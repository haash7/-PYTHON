day = input("enter the day").strip()
# remove leading and trailing spaces
attendees = int(input("enter the attendees"))

#Function in Python
def classifySuccessOfParty(day,attendees):
    weekdays = ["MON" , "TUE" , "WED" , "THU"]
    weekends = ["FRI" , "SAT" , "SUN"]

    if day not in weekdays and day not in weekends:
        return "INVALID DAY"
    if attendees < 0 :
        return "INVALID ATTENDEES"
    if day in weekdays :
        if 700 <= attendees <= 100:
            return "SUCCESSFULL"
        else:
            return "UNSUCCESSFULL"
    if day in weekends:
        if attendees >= 1500:
            return "SUCCESSFULL"
        else:
            return "UNSUCCESSFULL"


