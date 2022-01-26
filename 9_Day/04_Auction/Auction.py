bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # {"Anomymus": 123, "Jack": 321}
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("Your name pls: ")
    price = int(input("Yr bid pls: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Y/N: ").lower()
    if should_continue == "no" or should_continue == "n":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes" or should_continue == "y":
        bidding_finished = False