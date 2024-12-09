from art import logo
print(logo)
# TODO-1: Ask the user for input
bids = {}
name = input("What is you name?\n").lower()
bid = int(input("What is your bid\n"))
last = input("Are there any other bidders? Type 'yes or 'no'.").lower()

# TODO-2: Save data into dictionary {name: price}
bids[name]= bid
# TODO-3: Whether if new bids need to be added
last_person = False
while not last_person:
    if last == "yes":
        print("\n" * 20)
        name = input("What is you name?\n").lower()
        bid = int(input("What is your bid\n"))
        last = input("Are there any other bidders? Type 'yes or 'no'.").lower()
        bids[name] = bid

        last_person = False
    else:
        max_bid = max(bids.values())
        max_bidder = max(bids, key=bids.get)
        print(f"Congratulations {max_bidder}, you are the highest bidder with a bid of ${max_bid}!")
        last_person = True


# TODO-4: Compare bids in dictionary


