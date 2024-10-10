from art import logo

def clear_console():
    print("\n" * 100)

print(logo)
person = True
bidders = {}
winner = ''
while person is True:

    name_input = input('What is your name? ')
    ask_bid = input('What is your bid? ' )
    if ask_bid.isnumeric() is False:
        print("Please enter a numeric bid")
        continue
    bidders[name_input] = ask_bid
    person = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if person == "no":
        person = False
    else:
        person = True

    clear_console()

max_bid = 0
for name in bidders:
    if int(bidders[name]) > int(max_bid):
        max_bid = bidders[name]
        winner = name

print(f"The winner is {winner} with a bid of {max_bid}")
