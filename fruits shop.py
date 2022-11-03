import random
#generate_id = random.randrange(111111111, 999999999)
fruits = ["mango", "cherry", "orange", "pear"]
customer_category = int(input("what type of customer are you: 1 (regular_customer), 2 (special_customer) \n"))
if customer_category == 1:
    pref = input("which of these fruits would you prefer: cherry:50, mango:50, orange:100, banana:500\nEnter the name of the fruits\n ").lower()
    if pref in fruits:
        print("We have your prefered fruit")
    else:
        pref = input("Please, we don\'t have your prefered fruit. \nselect another\n ").lower()
    if pref in fruits:
        print("Hello, this is available")
    else:
        print("sorry, we can\'t help you")
    
    
elif customer_category == 2:
    generate_id = random.randrange(0000, 9999)
    print(generate_id)
    #pref = input("which of these fruits would you prefer: cherry, mango, orange, banana\nEnter the name of the fruits\n ").lower()
    id_number = int(input("Your id number: "))
    if id_number == generate_id:
        pref = input("which of these fruits would you prefer: cherry, mango, orange, banana\nEnter the name of the fruits\n ").lower()
    
    elif id_number != generate_id:
        re_enter = int(input("Please, you entered the wrong pin. \enter again\n "))
    
    #else:
        #print("sorry, we can\'t help you")     
    if pref in fruits:
        print("We have your prefered fruit")
    elif pref not in fruits:
        pref = input("Please, we don\'t have your prefered fruit. \nselect another\n ").lower()
    else:
        print("sorry, we can\'t help you")
    

    