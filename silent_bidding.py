from art import logo
print(logo)





bids={}

continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $ "))
    bids[name] = price
    more_or_no = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if more_or_no == 'no':
        continue_bidding = False
        winner=max(bids, key=bids.get)
        print(f"the winner is {winner} with ${bids[winner]}")

        # find_highest_bidder(bids)
    elif more_or_no == 'yes':
        print("\n"*20)





