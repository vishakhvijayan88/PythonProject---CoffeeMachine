import images
from Menu import MENU
import math



#user_order = str(input("What would you like to have (espresso/latte/cappuccino?: \n")).lower()

coffee_machine = {'Capacity': {'water': 3000, 'milk':2000, 'coffee': 300}, 'Levels':{'water':0, 'milk':0, 'coffee':0}, 'Money': 0}

coffee_options = ['espresso', 'latte', 'cappuccino']
start = input("Press Enter to see options: ")
print(f"Espresso: ${MENU['espresso']['cost']} \n"
      f"Latte: ${MENU['latte']['cost']} \n"
      f"Cappuccino: ${MENU['cappuccino']['cost']}")

#user_order = str(input("What would you like to have (espresso/latte/cappuccino)?: \n")).lower()


def check_levels(user_order, coffee_machine, MENU):

    if user_order == 'espresso':
        if coffee_machine['Levels']['water'] < MENU['espresso']['ingredients']['water']:
            print('Water level low. Refill Water.')

        if coffee_machine['Levels']['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print('Coffee level low. Refill Coffee.')
        return coffee_machine['Levels']['water'], coffee_machine['Levels']['coffee'], 0
    elif user_order == 'latte':
        if coffee_machine['Levels']['water'] < MENU['latte']['ingredients']['water']:
            print('Water level low. Refill Water.')
        if coffee_machine['Levels']['coffee'] < MENU['latte']['ingredients']['coffee']:
            print('Coffee level low. Refill Coffee.')
        if coffee_machine['Levels']['milk'] < MENU['latte']['ingredients']['milk']:
            print('Milk level low. Refill Milk.')
        return coffee_machine['Levels']['water'], coffee_machine['Levels']['coffee'], coffee_machine['Levels']['milk']
    elif user_order == 'cappuccino':
        if coffee_machine['Levels']['water'] < MENU['cappuccino']['ingredients']['water']:
            print('Water level low. Refill Water.')
        if coffee_machine['Levels']['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
            print('Coffee level low. Refill Coffee.')
        if coffee_machine['Levels']['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print('Milk level low. Refill Milk.')
        return coffee_machine['Levels']['water'], coffee_machine['Levels']['coffee'], coffee_machine['Levels']['milk']
    else:
        print(f"Water: {coffee_machine['Levels']['water']}")
        print(f"Milk: {coffee_machine['Levels']['milk']}")
        print(f"Coffee: {coffee_machine['Levels']['coffee']}")
        print(f"Money: {coffee_machine['Money']}")


#check_levels(user_order, coffee_machine, MENU)

def refill(coffee_machine, content):
    if coffee_machine['Levels'][str(content)] == coffee_machine['Capacity'][str(content)]:
        print(f"{str(content)} is already full")
    else:
        coffee_machine['Levels'][str(content)] = coffee_machine['Capacity'][str(content)]
        print(f"{content} level is now full.")
    return coffee_machine


def pay_amount(coffee_machine, user_order, MENU):
    coffee_machine['Money'] += MENU[str(user_order)]['cost']
    readytopay = input("Press 'Enter' when ready to pay. ")
    penny = int(input("How many pennies?: "))*0.01
    nickel = int(input("How many nickels?: "))*0.05
    dime = int(input("How many dimes?: "))*0.10
    quarter = int(input("How many quarters?: "))*0.25

    total = penny+nickel+dime+quarter
    #print(f"total: {total}") #test
    while total < MENU[user_order]['cost']:

        print(f"You are ${MENU[str(user_order)]['cost'] - total} short. Please insert more coins.")
        penny = penny + int(input("How many pennies?: "))*0.01
        nickel = nickel + int(input("How many nickels?: "))*0.05
        dime = dime + int(input("How many dimes?: "))*0.10
        quarter = quarter + int(input("How many quarters?: "))*0.25
        total = penny+nickel+dime+quarter

    denominations = [0.01, 0.05, 0.10, 0.25]
    difference_main = total - MENU[user_order]['cost']
    #print(f"difference_main: {difference_main}") #test
    difference = difference_main
    #print(f"difference: {difference}")
    change = 0
    coins = []
    if total == MENU[user_order]['cost']:
        print(f'Preparing your {user_order}...')
    else:
        j = 3
        while difference > 0 or j != -1:
            change = difference/denominations[j]
            #print(f"change: {change}") #test
            if change >= 1:
                coins.append(int(math.floor(change)))
            else:
                coins.append(0)
            #print(f"coins: {coins}") #test
            difference = difference - (denominations[j] * change)
            #print(f"calculation: {total}")#test
            #print(f"difference: {difference}") #test
            j -= 1

        #print(coins)#test
        print("Please collect your change")
        print(f"Total : ${difference_main}")
        print(f"Quarters : {coins[0]}")
        print(f"Dimes : {coins[1]}")
        print(f"Nickels : {coins[2]}")
        print(f"Pennies : {coins[3]}")
        print(f"Preparing your {user_order}...")
    return coffee_machine['Money']







loop = True
user_order = str(input("What would you like to have (espresso/latte/cappuccino)?: \n")).lower()
while loop == True:

    if user_order == 'report':
        print(f"water: {coffee_machine['Levels']['water']}")
        print(f"coffee: {coffee_machine['Levels']['coffee']}")
        print(f"milk: {coffee_machine['Levels']['milk']}")
        print(f"Money: {coffee_machine['Money']}")
    else:
        water_level, coffee_level, milk_level = check_levels(user_order, coffee_machine, MENU)
        if user_order == 'espresso':
            if water_level < MENU[str(user_order)]['ingredients']['water'] or coffee_level < MENU[str(user_order)]['ingredients']['coffee']:
                refillcheck = 'y'
                while refillcheck == 'y':
                    contentcheck = str(input("What would you like to refill (water, milk, coffee)?: "))
                    coffee_machine = refill(coffee_machine, contentcheck)
                    water_level, coffee_level, milk_level = check_levels(user_order, coffee_machine, MENU)
                    refillcheck = str(input("Would you like to refill anything else? y or n: "))
                    if refillcheck == 'n':
                        if user_order == 'espresso':
                            if water_level < MENU[str(user_order)]['ingredients']['water']:
                                print('Sorry, cannot proceed without refilling water')
                                refillcheck = 'y'
                            elif coffee_level < MENU[str(user_order)]['ingredients']['coffee']:
                                print('Sorry, cannot proceed without refilling coffee')
                                refillcheck = 'y'
                        else:
                            if water_level < MENU[str(user_order)]['ingredients']['water']:
                                print('Sorry, cannot proceed without refilling water')
                                refillcheck = 'y'
                            elif coffee_level < MENU[str(user_order)]['ingredients']['coffee']:
                                print('Sorry, cannot proceed without refilling coffee')
                                refillcheck = 'y'
                            elif milk_level < MENU[str(user_order)]['ingredients']['milk']:
                                print('Sorry, cannot proceed without refilling milk')
                                refillcheck = 'y'
                            elif water_level >= MENU[str(user_order)]['ingredients']['water'] and coffee_level >= \
                                    MENU[str(user_order)]['ingredients']['coffee'] and milk_level >= \
                                    MENU[str(user_order)]['ingredients']['milk']:
                                print('All ingredients are full. Please proceed to payment')
                                refillcheck = 'n'
        else:
            if water_level < MENU[str(user_order)]['ingredients']['water'] or coffee_level < \
                    MENU[str(user_order)]['ingredients']['coffee'] or milk_level < MENU[str(user_order)]['ingredients'][
                'milk']:
                refillcheck = 'y'
                while refillcheck == 'y':
                    contentcheck = str(input("What would you like to refill (water, milk, coffee)?: "))
                    coffee_machine = refill(coffee_machine, contentcheck)
                    water_level, coffee_level, milk_level = check_levels(user_order, coffee_machine, MENU)
                    refillcheck = str(input("Would you like to refill anything else? y or n: "))
                    if refillcheck == 'n':
                        if user_order == 'espresso':
                            if water_level < MENU[str(user_order)]['ingredients']['water']:
                                print('Sorry, cannot proceed without refilling water')
                                refillcheck = 'y'
                            elif coffee_level < MENU[str(user_order)]['ingredients']['coffee']:
                                print('Sorry, cannot proceed without refilling coffee')
                                refillcheck = 'y'
                        else:
                            if water_level < MENU[str(user_order)]['ingredients']['water']:
                                print('Sorry, cannot proceed without refilling water')
                                refillcheck = 'y'
                            elif coffee_level < MENU[str(user_order)]['ingredients']['coffee']:
                                print('Sorry, cannot proceed without refilling coffee')
                                refillcheck = 'y'
                            elif milk_level < MENU[str(user_order)]['ingredients']['milk']:
                                print('Sorry, cannot proceed without refilling milk')
                                refillcheck = 'y'
                            elif water_level >= MENU[str(user_order)]['ingredients']['water'] and coffee_level >= \
                                    MENU[str(user_order)]['ingredients']['coffee'] and milk_level >= \
                                    MENU[str(user_order)]['ingredients']['milk']:
                                print('All ingredients are full. Please proceed to payment')
                                refillcheck = 'n'


    if user_order in ('espresso', 'latte', 'cappuccino'):
        coffee_machine['Money'] = pay_amount(coffee_machine, user_order, MENU)
    if user_order == 'espresso':

        coffee_machine['Levels']['water'] -= MENU[str(user_order)]['ingredients']['water']
        coffee_machine['Levels']['coffee'] -= MENU[str(user_order)]['ingredients']['coffee']
    elif user_order in ['latte', 'cappuccino']:
        coffee_machine['Levels']['water'] -= MENU[str(user_order)]['ingredients']['water']
        coffee_machine['Levels']['coffee'] -= MENU[str(user_order)]['ingredients']['coffee']
        coffee_machine['Levels']['milk'] -= MENU[str(user_order)]['ingredients']['milk']
    print(f"Your {user_order} is ready.")
    user_order = str(input("What would you like to have (espresso/latte/cappuccino)?: \n")).lower()