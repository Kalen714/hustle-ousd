checking = "yes"
#while checking == "yes":
    #print("What is your age: ")
    #user_input = input ()
    #if int(user_input) >= 18:
        #print("Yes you can vote")
    #else:
        #print ("You can't vote")
    #print("Would you like to check another age?")
    #user_input2 = input ( )
    #checking = user_input2
List = [-9,7,0]
for i in List:
    if i > 0:
        print('positive')
    elif i < 0:
        print('negative')
    else:
        print('0')  
inventory = ["tnt","glass","grass","netherite","Waxed Lightly Weathered Chiseled Copper Stairs"]
for i in inventory:
    if i == "Waxed Lightly Weathered Chiseled Copper Stairs":
        print("Why do you have this in your inventory?")
    elif i == "tnt":
        print("tnt")