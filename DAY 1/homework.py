x=int(input("enter the total no of vehicles :"))
y=int(input("enter the total no of wheels :"))
for two_wheelers in range(0, x + 1):
    four_wheelers = x - two_wheelers   
    
    wheels_count = (two_wheelers * 2) + (four_wheelers * 4)
    if wheels_count == y:
        print("\n--- Result Found ---")
        print("Two-wheelers:", two_wheelers)
        print("Four-wheelers:", four_wheelers)
        break  
    