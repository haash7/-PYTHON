total_tickets = int(input("enter the total no of tickets : "))
ticket_price  = int(input("enter the price of each ticket :"))
amount = total_tickets * ticket_price
category = int(input("enter the category type 0 or 1"))
discount = 0
if total_tickets > 15 :
    discount+= 20;
if  category == 1 :
    discount+= 5;
if discount>0:
    amount=amount-(amount*discount/100)
    if total_tickets>15 and category ==1:
        print("Discount applied - 1.MAx Ticket and 2.Student")
    elif total_tickets > 15 :
        print("MAximum Dicount applied")
    else :
        print("Student Discount applied")
else:
    print( " NO discount is appled ")
print (" total Amount " , amount)                    
