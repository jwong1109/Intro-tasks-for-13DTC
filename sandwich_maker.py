"""Sandwich Maker
"""

# Bread options
wholemeal = 1
white = 0.8
cheesy_white = 1.20
gluten_free = 1.40

# Meat options
chicken = 2.69
beef = 3
salami = 4
vegan_slice = 3.30

# Garnish options
onion = 1.69
tomato = 1.00
lettuce = 2.00
cheese = 2.50


# Choose Bread function
def choose_bread():
    bread_choice = input(f"Choose an option for your bread: \n Wholemeal "
                         f"${wholemeal:,.2f} \n "
                         f"White ${white:,.2f} \n Cheesy White "
                         f"${cheesy_white:,.2f} \n Gluten "
                         f"Free ${gluten_free:,.2f}"
                         f"\n-> ").lower()
    if bread_choice != "wholemeal" and bread_choice != "white" and \
            bread_choice != "cheesy white" and bread_choice != "gluten free":
        choose_bread()

    return bread_choice


# Choose Meat function
def choose_meat():
    meat_choice = ""
    meat_list = []
    while meat_choice != "N":
        meat_choice = input(f"\nSelect the meat: \n Chicken $"
                            f"{chicken:,.2f} \n Beef ${beef:,.2f} \n Salami "
                            f"${salami:,.2f} \n Vegan Slice $"
                            f"{vegan_slice:,.2f}"
                            f"\n -> ").lower()
        if meat_choice != "chicken" and meat_choice != "beef" and \
                meat_choice != "salami" and meat_choice != "vegan slice":
            choose_meat()
        meat_list.append(meat_choice)
        meat_choice = input("Would you like any more meat? (Y or N) ").title()
    return meat_list


# Choose Garnish function
def choose_garnish():
    garnish_choice = ""
    garnish_list = []
    while garnish_choice != "N":
        garnish_choice = input(f"\nSelect the garnish: "
                               f"\n Onion ${onion:,.2f} \n "
                               f"Tomato ${tomato:,.2f} \n "
                               f"Lettuce ${lettuce:,.2f} \n "
                               f"Cheese ${cheese:,.2f}"
                               f"\n -> ").lower()
        if garnish_choice != "onion" and garnish_choice != "tomato" \
                and garnish_choice != "lettuce" and garnish_choice != "cheese":
            choose_garnish()
        garnish_list.append(garnish_choice)
        garnish_choice = input("Would you like any more garnish? (Y or "
                               "N): ").title()
    return garnish_list


# Calculate Cost function
def calculate_cost(calculate_bread, calculate_meat, calculate_garnish):
    count_bread = 0
    if calculate_bread == "gluten free":
        count_bread = gluten_free
    elif calculate_bread == "white":
        count_bread = white
    elif calculate_bread == "cheesy white":
        count_bread = cheesy_white
    elif calculate_bread == "wholemeal":
        count_bread = wholemeal
    print(f"\nBread cost: ${count_bread:,.2f}")

    count_meat = 0
    for meat in calculate_meat:
        if meat == "chicken":
            count_meat += chicken
        elif meat == "vegan slice":
            count_meat += vegan_slice
        elif meat == "salami":
            count_meat += salami
        elif meat == "beef":
            count_meat += beef
    print(f"Meat(s) cost: ${count_meat:,.2f}")

    count_garnish = 0
    for garnish in calculate_garnish:
        if garnish == "onion":
            count_garnish += onion
        elif garnish == "tomato":
            count_garnish += tomato
        elif garnish == "lettuce":
            count_garnish += lettuce
        elif garnish == "cheese":
            count_garnish += cheese
    print(f"Garnish(s) cost: ${count_garnish:,.2f}")

    calculate_sandwich = count_bread + count_meat + count_garnish
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"The total cost for your order is "
                        f"${calculate_sandwich:,.2f}! \n "
                        f"Confirm (Y) or make a change (N)? ").title()
    if confirm == "Y":
        return calculate_sandwich
    else:
        return change_options(calculate_bread, calculate_meat,
                              calculate_garnish)


# Change options function
def change_options(change_bread, change_meat, change_garnish):
    change = ""
    while change != "bread" and change != "meat" and change != "garnish" and\
            change != 'x':
        change = input("\n What part do you want to change? "
                       "('x' to stop changes) ").lower()
    if change == "bread":
        change_bread = choose_bread()
    elif change == "meat":
        change_meat = choose_meat()
    elif change == "garnish":
        change_garnish = choose_garnish()

    changed_cost = calculate_cost(change_bread, change_meat, change_garnish)
    return changed_cost


# Main Routine
bread_option = choose_bread()
meat_option = choose_meat()
garnish_option = choose_garnish()

cost = calculate_cost(bread_option, meat_option, garnish_option)
print()
print(f"You have proceeded to the checkout to pay ${cost:,.2f}! Thanks")
