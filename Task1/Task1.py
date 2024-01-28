price_of_pizza = 12
delivery = 2.5
Tuesday_discount = .5
app_discount = .75
total_price = 0

yes_list = ["y","yes"]
no_list = ["n", "no"]

while True:
    try:
        pizza_input = int(input("How many pizza did the customer order? "))
        if pizza_input > 0:
            total_price = pizza_input * price_of_pizza  
            break   
        else:
            print("Please Enter a positive integer!")
            continue
    except ValueError:
        print("Please enter a number!")
        continue

while True:
    delivery_input = input("Is delivery required? ").lower()
    if delivery_input in yes_list and pizza_input >= 5:
        break
    elif  delivery_input in yes_list:
        total_price += delivery
        break
    elif delivery_input in no_list:
        break
    else:
        print("Please answer \"Y\" or \"N\" ")
        continue

while True:
    tuesday_input = input("Is it Tuesday? ").lower()
    if tuesday_input in yes_list:
        total_price *= Tuesday_discount
        break
    elif tuesday_input in no_list:
        break
    else:
        print("Please answer \"Y\" or \"N\" ")
        continue


while True:
    app_input = input("Did the customer use the app? ").lower()
    if app_input in yes_list:
        total_price *= app_discount
        break
    elif app_input in no_list:
        break
    else:
        print("Please answer \"Y\" or \"N\" ")
        continue


print(f"Total Price: €{total_price:.2f}.")

