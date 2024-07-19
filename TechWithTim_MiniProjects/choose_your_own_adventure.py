name = input("Type your name:  ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go?"  ).lower()

# option left
if answer == "left":
    answer = input("You have arrived to a river. You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across:  ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator. You lose.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You lose.")
    else:
        print("Not a valid option. You lose.")

# option right
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Dou you want to cross it or head back? (cross/back)  ").lower()
    
    # options back and cross
    if answer == "back":
        print("You go back to the main road. You lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no)").lower()

        # options yes and no
        if answer == "yes":
            print("You talked to the stranger and they give you gold. You win.")
        elif answer == "no":
            print("You ignored the stranger and they were offended. You lose.")
        else:
            print("Not a valid option. You lose.")
        # options yes and no

    else:
        print("Not a valid option. You lose.")
    # options back and cross

else:
    print("Not a valid option. You lose.")

print("Thank you for trying the game,", name)