#concession program
tickets = {"adult": 10.00, "child": 5.00, "senior": 7.50}

menu = {
    "popcorn": 5.00,
    "sweets": 2.50,
    "drinks": 3.00,
    "nachos": 4.50,
    "french fries": 6.00,
    "hot dog": 6.50,
    "ice cream": 3.50}

print("----------TICKET PRICES----------")
for ticket_type, price in tickets.items():
    print(f"{ticket_type} ticket: £{price:.2f}")
print("---------------------------------")

print("----------MENU----------")
for item, price in menu.items():
    print(f"{item}: £{price:.2f}")
print("------------------------")

print("Welcome to the cinema!")
choice = input("Would you like to order or pay for your tickets? (order/pay/both): ").lower()
total = 0
total1 = 0

if choice == "order" or choice == "both":
    order = input("Please order an item from the menu above: ").strip().lower()
    while True:
        if order in menu:
            total += menu[order]
            choice2 = input(f"You have ordered {order} for £{menu[order]:.2f}. Would you like to order anything else? (yes/no): ").strip().lower()
            if choice2 == "no":
                print(f"Your total is £{total:.2f}. Thank you for your order!")
                break
            elif choice2 == "yes":
                order = input("Please order another item from the menu above: ").strip().lower()
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid item. Please try again.")

if choice == "pay" or choice == "both":
    ticket_type = input("Please enter the type of ticket you would like to purchase (adult/child/senior): ").strip().lower()
    amount = int(input("Please enter the number of tickets you would like to purchase: "))
    if ticket_type in tickets:
        total1 += tickets[ticket_type] * amount
        print(f"You have purchased {amount} {ticket_type} ticket(s) for £{total1:.2f}.")
        print("Thank you for your purchase! Enjoy the movie!")