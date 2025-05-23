import time

MENU = {
    "espresso":     {"ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 50},
    "latte":        {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 75},
    "cappuccino":   {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 100},
    "mocha":        {"ingredients": {"water": 100, "milk": 100, "coffee": 20, "chocolate": 10}, "cost": 110},
    "americano":    {"ingredients": {"water": 300, "milk": 0, "coffee": 18}, "cost": 60},
    "flat white":   {"ingredients": {"water": 150, "milk": 150, "coffee": 24}, "cost": 90},
    "macchiato":    {"ingredients": {"water": 50, "milk": 30, "coffee": 18}, "cost": 70},
    "irish coffee": {"ingredients": {"water": 200, "milk": 50, "coffee": 24, "whiskey": 15}, "cost": 150}
}

resources = {"water": 1000, "milk": 600, "coffee": 300, "chocolate": 50, "whiskey": 30, "money": 0}

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_menu():
    print("\n🤗 WELCOME TO THE VIRTUAL COFFEE MACHINE ☕")
    print("\n COFFEE MENU:")
    for drink, info in MENU.items():
        print(f"➡️  {drink.capitalize()} -> Rs{info['cost']}")
    print("\nType 'report' to view resources.\n")

def is_enough(ingredients):
    for item in ingredients:
        if item not in resources or ingredients[item] > resources[item]:
            print(f"❌ Sorry, not enough {item}.")
            return False
    return True

def process_payment(cost):
    print("🪙 Please insert coins")
    total = 0
    try:
        total += int(input("   👉 How many 5Rs coins? ")) * 5
        total += int(input("   👉 How many 10Rs coins? ")) * 10
        total += int(input("   👉 How many 20Rs coins? ")) * 20
    except ValueError:
        print("⚠️ Invalid input. Transaction cancelled.")
        return 0
    if total < cost:
        print("❌ Not enough money. Money refunded.")
        return 0
    if total > cost:
        change = total - cost
        print(f"💸 Here is your Rs{change} in change.")
    return cost

def make_coffee(name, ingredients):
    print("\n🔧 Starting your drink...\n")
    time.sleep(0.8)
    print("🫘 Grinding beans...")
    time.sleep(1.2)
    print("💧 Boiling water...")
    time.sleep(1.2)
    if ingredients.get("milk", 0) > 0:
        print("🥛 Steaming milk...")
        time.sleep(1)
    if ingredients.get("chocolate", 0) > 0:
        print("🍫 Adding chocolate...")
        time.sleep(1)
    if ingredients.get("whiskey", 0) > 0:
        print("🥃 Adding Irish twist...")
        time.sleep(1)
    print("🌀 Brewing coffee...")
    time.sleep(1.2)
    print()

    # Bold output
    print(f"\033[1m☕ HERE IS YOUR {name.upper()}! ENJOY 😊\033[0m\n")

    for item in ingredients:
        resources[item] -= ingredients[item]

def print_report():
    print("\n📊 Machine Report:")
    print(f"💧 Water: {resources.get('water', 0)}ml")
    print(f"🥛 Milk: {resources.get('milk', 0)}ml")
    print(f"🫘 Coffee: {resources.get('coffee', 0)}g")
    print(f"🍫 Chocolate: {resources.get('chocolate', 0)}g")
    print(f"🥃 Whiskey: {resources.get('whiskey', 0)}ml")
    print(f"💵 Money: Rs{resources['money']}\n")

def coffee_machine():
    while True:
        show_menu()
        choice = input("👉 What would you like? (Espresso/Latte/Cappuccino/Mocha/Americano/Flat white/Macchiato/Irish coffee) -> ").lower()

        if choice == 'off':
            print("👋 Turning off... Have a great day!")
            break
        elif choice == 'report':
            print_report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_enough(drink["ingredients"]):
                payment = process_payment(drink["cost"])
                if payment:
                    resources["money"] += payment
                    make_coffee(choice, drink["ingredients"])
        else:
            print("❓ Invalid choice. Please try again.\n")

# Run the machine
coffee_machine()
