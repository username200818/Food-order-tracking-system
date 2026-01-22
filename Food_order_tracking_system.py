food_orders = []

def place_order():
    customer = input("Enter customer name: ")
    food = input("Enter food item: ")
    quantity = int(input("Enter quantity: "))
    food_orders.append({
        "customer": customer,
        "food": food,
        "quantity": quantity
    })
    print("Food order placed successfully")

def view_orders():
    if not food_orders:
        print("No food orders found")
    else:
        for o in food_orders:
            print("Customer:", o["customer"])
            print("Food:", o["food"])
            print("Quantity:", o["quantity"])
            print("------------------")

def main():
    while True:
        print("1. Place Order")
        print("2. View Orders")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            place_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
