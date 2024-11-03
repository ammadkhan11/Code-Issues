#TODO: 1. menu in dictionary
MENU = {
   "espresso": {
       "ingredients": {
       "water": 50,
       "coffee": 18,
       },
       "cost": 1.5,
   },
   "latte": {
       "ingredients": {
           "water": 200,
           "coffee": 24,
           "milk":150
       },
       "cost": 2.5,
   },
   "cappuccino":{
       "ingredients": {
           "water": 250,
           "coffee": 24,
       },
       "cost": 3.00,
   }

}

water_ini =300
coffee_ini =100
milk_ini =200
money_ini =0.0

quarter=0.25
nickel=0.05
dime=0.10
penny=0.1

def coffee_machine(water_initial,coffee_initial,milk_initial,money_initial):
    water=water_initial
    coffee=coffee_initial
    milk=milk_initial
    money=money_initial
    
    #TODO: 2. taking input
    user_input=input("Dear customer which type of coffee do you want?press espresso,latte,cappuccino,exit\n").lower()

    if user_input=="espresso" and (water <50 or coffee <18):
        order="False"
        print(" Sorry, there are not enough ingredients")
        exit()
    if user_input=="latte" and (water <200 or coffee <24 or milk <150) :
        order="False"
        print(" Sorry, there are not enough ingredients")
        exit()
    if user_input=="cappuccino" and (water <250 or coffee <24):
        order="False"
        print(" Sorry, there are not enough ingredients")
        exit()

    if user_input=="espresso":
        water=(water-MENU["espresso"]["ingredients"]["water"])
        coffee=(coffee-MENU["espresso"]["ingredients"]["coffee"])
        bill_to_pay = MENU["espresso"]["cost"]
    elif user_input=="latte":
        water=(water-MENU["latte"]["ingredients"]["water"])
        coffee=(coffee-MENU["latte"]["ingredients"]["coffee"])
        milk=milk-MENU["latte"]["ingredients"]["milk"]
        bill_to_pay = MENU["latte"]["cost"]

    elif user_input=="cappuccino":
        water=(water-MENU["cappuccino"]["ingredients"]["water"])
        coffee=(coffee-MENU["cappuccino"]["ingredients"]["coffee"])
        bill_to_pay = MENU["cappuccino"]["cost"]

    else:
        exit()

    #TODO: 3. making report of machine

    def report():
        print(f"{water}ml")
        print(f"{coffee}g")
        print(f"{milk}ml")
        print(f"{money}$")

    report()

    order="True"

    #TODO: 4. Resources are sufficient or not
    


    required_bill="True"

    print(f"your total bill is{bill_to_pay:.4f}")

    if order=="True":
        print("Please enter the money\n")
        num_quarters=int(input("How many quarters do you insert?\n"))
        num_dimes=int(input("How many dimes do you insert?\n"))
        num_nickels=int(input("How many nickels do you insert?\n"))
        num_pennies=int(input("How many pennies do you insert?\n"))
        Bill=(quarter*num_quarters)+(dime*num_dimes)+(penny*num_pennies)+(nickel*num_nickels)
        if(Bill < bill_to_pay):
            print("\nSorry you have not inserted enough money, Money refunded")
        else:
            change= Bill - bill_to_pay
            money = money + bill_to_pay
            print(f"\nYour change money is {change}$\nENJOY YOUR COFFEE")
    report()
    coffee_machine(water, coffee, milk, money)
coffee_machine(water_ini, coffee_ini, milk_ini, money_ini)
exit()
