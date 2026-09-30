#START
#Ask the user about how much money he has
#STORE the input
#IF money(input) is less than 1000
#   DISPLAY "It is still to early to buy a new phone"
#ELSE IF money(input) is less than 2000
#   DISPLAY "Save a little more"
#ELSE IF money(input) is less than 3200
#   DISPLAY "You are almost there."
#ELSE 
#   DISPLAY "Congratulations! You can buy a new phone."
#END

money = int(input("How much money do you have? "))

if money < 1000:
    print("It is still to early to buy a new phone")
elif money < 2000:
    print("Save a little more")
elif money < 3200:
    print("You are almost there.")
else:
    print("Congratulations! You can buy a new phone.")
