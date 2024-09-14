from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James", "321"}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))

  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
########################################################################################################## 
#Another version:
##########################################################################################################
def biders_adder(users,bid):
    dic={}
    dic['name'] = users
    dic['bid'] = bid
    biders.append(dic)
    return biders
biders = []
max_bid=0
winner =[]

bids = {}
#ask your if they want to restart
bidder_on = True
while bidder_on:
    users = input("What is your name ? : ")
    bid = int(input('What is your bid? :$ '))
    
    #calling function
    biders_adder(users,bid)    
    
    reset= input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if reset == 'no':
        bidder_on = False
        for n in range(0,len(biders)):
            if biders[n]['bid'] > max_bid:
                max_bid = biders[n]['bid']
                winer = biders[n]
            else:
                max_bid = max_bid
                
        print(winer)
        print('Good Bye!')


