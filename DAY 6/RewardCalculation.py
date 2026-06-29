class VISAcard:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
    
    
    def display_details(self):
        print(self.holder_name)
        print(self.card_number)

    def compute_reward(self,amount):
        reward = amount*0.01
        print("the reward for VISA card is:",reward)    

class HPVISAcard(VISAcard):
    def compute_reward(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="Fuel":
            reward+=10
        print("reward for HPVISA card is :", reward)

#INPUT
card_type=input("enter VISA/HPVISA ").strip()
if card_type not in ["VISA","HPVISA"]:
    print("invalid card choice")
else:
    holder_name=input("enter the holder_ name :").strip()
    card_number=input("enter the card_number :").strip() 
    amount=float(input("enter the amount:"))
    purchase_type=input("enter the purchase_type :").strip() 


    if card_number=="VISA":
        card=VISAcard(holder_name,card_number)
    else:
        card=HPVISAcard(holder_name,card_number)


card.display_details()
card.compute_reward(purchase_type,amount)                      







