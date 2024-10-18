print('''
       ___________________________________________,
   ___/  ////////  \____/                         |
  <__ |_////////__________________________________|
    \)                 *                |________|
     /        __________________________|
    /        /  ||   //
   /        /____\__//
  /        /~~~~~~~~~
 /        /
/        /
\-------/
''')
print("You've been busted by the cops dealing weed")
dir1 = input("Your mission is to escape, Choose a direction to head to, left or right ? \n").strip().lower()

if dir1 == "left":
    print("You tried to go to left, but got shot by a spy.")
    exit()
elif dir1 == "right":
    print("You've managed to find a cheap motel near the beach")
    choice2 = input("Now, do you want to escape the country or wait ? type escape or wait \n").strip().lower()
    if choice2 == "escape":
        print("You booked a flight . . .")
        print("You got caught by the cops at the airport.")
        exit()
    elif choice2 == "wait":
        print("You went underground . .")
        choice3 = input("The cops arent actively looking for you now, would you go back to your town, go to the nearest city or go to the country-side? Type town, city or countryside \n").strip().lower()
        if choice3 == "town":
            print("You went back to your town and got jumped by cops.")
            exit()
        elif choice3 == "city":
            print("You tried going to the nearest cities but all the bridges were blocked by cops, you got arrested.")
            exit()
        elif choice3 == "countryside":
            print("You drove to the country side through he rural roads. . . ")
            print("A long time later, the cops stopped finding you, You win !")     
else:
    print("Please enter a valid option.")
    exit()
