# Chap 3 Bonus Ex: Burger Shack Vendor


# Defining Function for displaying the menu
def display_menu():
    # Displaying the welcome message and the menu options
    print("Welcome to Burger Shack!")
    print("1. Burger Types: Beef, Chicken, Vegetarian")
    print("2. Toppings: Cheese, Peanut Butter, Avocado")
    print("3. Condiments: Ketchup, Mayonnaise, BBQ Sauce")
    print("4. Sides: Fries, Drink")

# Defining function for placing order
def place_order():
    # Initializing an empty order dictionary
    order = {
        "burger_type": None,
        "toppings": [],
        "condiments": [],
        "sides": []
    }

    try:
        # Choosing burger type
        burger_choice = int(input("Select Burger Type (1-3): "))
        burger_types = ["Beef", "Chicken", "Vegetarian"]
        order["burger_type"] = burger_types[burger_choice - 1]

        # Adding toppings
        print("\nChoose Toppings (Enter 0 to finish):")
        toppings = ["Cheese", "Peanut Butter", "Avocado"]
        while True:
            topping_choice = int(input("   Topping (1-3): "))
            if topping_choice == 0:
                break
            order["toppings"].append(toppings[topping_choice - 1])

        # Adding condiments
        print("\nChoose Condiments (Enter 0 to finish):")
        condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
        while True:
            condiment_choice = int(input("   Condiment (1-3): "))
            if condiment_choice == 0:
                break
            order["condiments"].append(condiments[condiment_choice - 1])

        # Adding sides
        print("\nChoose Sides (Enter 0 to finish):")
        sides = ["Fries", "Drink"]
        while True:
            side_choice = int(input("   Side (1-2): "))
            if side_choice == 0:
                break
            order["sides"].append(sides[side_choice - 1])

        return order
    except (ValueError, IndexError): # Codes for errors
        print("Invalid input. Please enter a valid choice.")

# Defining function for order calculation
def calculate_total(order):
    # Assuming the fixed costs for items
    burger_cost = 5.00
    topping_cost = 1.50
    condiment_cost = 1.00
    side_cost = 2.50

    # Calculating the total cost based on the order
    total_cost = burger_cost + len(order["toppings"]) * topping_cost + len(order["condiments"]) * condiment_cost \
                 + len(order["sides"]) * side_cost

    return total_cost


# Defining function for payment process
def process_payment(total_cost):
    try:
        # Getting the amount paid from the user
        amount_paid = float(input(f"\nTotal Cost: {total_cost:.2f} AED\nEnter Amount Paid: "))

        # Checking if the payment is sufficient and provide change if needed
        if amount_paid >= total_cost:
            change = amount_paid - total_cost
            print(f"Payment successful! Change: {change:.2f} AED")
        else:
            print("Insufficient payment. Please provide enough funds.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Defining main function for ordering process
def main():
    # Executing the main ordering process
    display_menu()
    order = place_order()
    total_cost = calculate_total(order)
    process_payment(total_cost)


if __name__ == "__main__":
    main()