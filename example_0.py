import random

def select_menu():
    menu = {
        #Coffee
        "Espresso Con Panna": {"price": 135, "type": "Coffee"},
        "Espresso": {"price": 85, "type": "Coffee"},
        "Cafe Latte": {"price": 135, "type": "Coffee"},
        "Cafe Mocha": {"price": 135, "type": "Coffee"},
        "Cappucino": {"price": 135, "type": "Coffee"},
        "Macchiato": {"price": 85, "type": "Coffee"},
        "Americano": {"price": 85, "type": "Coffee"},
        #Dessert
        "New York Cheesecake": {"price": 65, "type": "Dessert"},
        "Souffle": {"price": 85, "type": "Dessert"},
        "Brownies": {"price": 60, "type": "Dessert"},
        "Mousse Cake": {"price": 55, "type": "Dessert"},
        "Fruit Tart": {"price": 75, "type": "Dessert"},
        "Special": {"price": 170, "type": "Dessert"},
        #Light meal
        "Pasta": {"price": 250, "type": "Light meal"},
        "Risotto": {"price": 80, "type": "Light meal"},
        "Panini": {"price": 120, "type": "Light meal"},
        
        
    }
    
    order = {}
    total_price = 0
    print("=== Welcome to SLEEPWALKER ===")
    while True:
        print("Please select a dish (enter dish name or number, enter 'done' to finish):")
        types = set(dish["type"] for dish in menu.values())
        types = list(types)
        types.sort()

        print(types)
        for t in types:
            print(f"{t}:")
            for i, dish in enumerate(menu.keys(), start=1):
                #print(f"{i}. {dish}(${menu[dish]['price']})")
                if menu[dish]["type"] == t:
                    print(f"{i}. {dish}(${menu[dish]['price']})")


        # prevType = ""
        # for i, dish in enumerate(menu.keys(), start=1):
        #     # if menu[dish]["type"] == t:
        #     if menu[dish]['type'] != prevType:
        #         print(f"{menu[dish]['type']}:")
        #         prevType = menu[dish]['type']
        #     print(f"{i}. {dish}(${menu[dish]['price']})")
        choice = input("Enter: ")
        if choice == "done":
            break
        try:
            choice = int(choice)
            dish = list(menu.keys())[choice - 1]
        except (ValueError, IndexError):
            dish = choice
        if dish not in menu:
            print("Invalid dish, please select again")
            continue
        if dish in order:
            order[dish] += 1
        else:
            order[dish] = 1
        total_price += menu[dish]["price"]
        print(f"{dish} has been added to your order")
    print("Order details:")
    for dish, quantity in order.items():
        price = menu[dish]["price"]
        dish_total = price * quantity
        print(f"{dish} x {quantity} ${price} = ${dish_total}")
    print(f"Total Price: ${total_price}")
    
    # Lottery function
    if total_price >= 300:
        print("Congratulations! You've earned a chance to enter the lottery!")
        lottery_results = ["No Prize", "Lucky Prize", "No Prize", "No Prize"]
        result = random.choice(lottery_results)
        if result == "No Prize":
            print("Sorry, you didn't win any prize this time.")
        else:
            print(f"You've won: {result}")

select_menu()