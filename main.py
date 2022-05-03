"""Integration project: Genshin Impact Wish simulator"""
__author__ = "Jaime Ortega"


def main():
    """
    This function will allow for the whole program to run.The
    purpose of this program is to add the primogems from
    the different ways you can earn them and the amount you
    have will let you input how much wishes you have and then let
    you "roll" for characters or weapons.
    :return:
    """

    def daily_commissions():
        """
        This function serves to calculate the primogems from daily
        commissions.It will ask the user to input how many they
        complete and calculate it and total it.
        :return:
        """
        while True:
            # The while true runs until a condition is false. The try and
            # except will only run once the try is tested and no exception
            # is found however once an exception is found, the exception
            # parts run so in the code below when you enter a letter it
            # will tell you to input a number
            try:
                primogems_daily = int(input("How many daily commissions did "
                                            "you do? "))
                primogems_awarded = 40
                primogems_earned = primogems_daily * primogems_awarded
                print("You earned ", primogems_earned, "primogems")
                break
            except ValueError:
                print("ERROR!!! Only numbers")

    def storyline_primo():
        """
        This function serves to calculate the amount earned from completing
        the storylines in the game.The user gets 60 primogems per
        quest so in this function we get how many storylines
        they did multiplied by 60.
        :return:
        """
        while True:
            # The while true and try and except will allow for my
            # program to run with only numbers inputted and if
            # the user inputs a letter it will prompt them to enter again.
            try:
                primogems_storyline = int(input("How many storylines did you"
                                                " complete? "))
                # For each storyline completed in the game you are
                # you are awarded 60 primogems
                primogems_storyline_awarded = 60
                primogems_storyline_earned = \
                    primogems_storyline * primogems_storyline_awarded
                print("You earned", primogems_storyline_earned, "primogems")
                break
            except ValueError:
                print("ERROR!!! Only numbers")

    def farming_for_primogems():
        """
        This function serves to calculate the amount made from farming.
        So in the game you can get primogems from farming and you get around
        5 each time so you enter how many small quests you completed
        and it multiply those together.

        :return:
        """
        while True:  # https://stackoverflow.com/questions/23326099/how-can-
            # i-limit-the-user-input-to-only-integers-in-python#:~:text=
            # The%20best%20way%20would%20be,the%20message%20to%20take%20input.
            # &text=So%20when%20you%20want%20an,the%20float%20as%20a%20param
            # eter.

            # This while true and try and except serve to make sure the user
            # does not enter a input that makes the program crash and prompts
            # them to enter the write value such as an integer and not a
            # letter.
            try:
                primogems_farming = \
                    int(input("How many small quests did you complete? "))
                primogems_farming_awarded = 5
                primogems_farming_earned = \
                    primogems_farming * primogems_farming_awarded
                print("You earned", primogems_farming_earned, "primogems")
                break
            except ValueError:
                print("ERROR!!! Only numbers")

    def wish_total():
        """
        This functions serves to add the grand totals of
        the other function to add them to see how much
        wishes they can get.
        :return:
        """
        daily_commissions()
        farming_for_primogems()
        storyline_primo()
        total_count_of_primogems = int(input("Please enter the total amount"
                                             " of primogems gained from"
                                             " farming, daily commissions "
                                             " and storylines: "))
        amount_for_wishes = int(total_count_of_primogems / 160)
        print(amount_for_wishes)
        # Your going to be wishing on Kazuha character banner and the
        # items below are what are on his banner
        import random
        # From https://pynative.com/python-random-choice/
        wishing_banner_list = ['Rust', 'The Flute', 'The Widsith',
                               'Sacrificial Greatsword', 'Razor',
                               'Bennet', 'Mona', 'Kazuha', 'Jean']
        total_wishes = int(input("How much wishes do you have?"))
        print("Since you have", total_wishes, "wishes,"
                                              "You'll see what you rolled "
                                              "below")
        # The for loop below allows for items to be selected from
        # the list above depending on the number of wishes the user inputted
        for x in range(total_wishes):
            wishing = random.choice(wishing_banner_list)
            print(wishing)
        print("Would you like to keep going or end the program?")
        user_choice = input("Enter 1 to end the program "
                            " or Enter 2 to continue it: ")
        # User can choose from the selection below to either go to another
        # portion of the program or to end it.The else acts as a safety net
        # because if the user inputs a wrong value it prompts them again
        # to enter the correct value.
        if user_choice == 1:
            end_of_program()
        elif user_choice == 2:
            mora_calculator()
        else:
            print("ERROR!!!ERROR!!Please input a either 1 or 2,"
                  " only numbers!!!!")
            wish_total()

    def mora_calculator():
        """
        This function asks user for what level do they want to upgrade
        their character too.Each level cost 6000 mora so
        all you have to do is multiply the level you want by 6000.Mora
        is the in game currency.
        :return:
        """
        try:
            print("In Genshin Impact you need mora in order to"
                  " upgrade a character \nand it goes by levels of"
                  " 1")
            character_level = int(input("What level do you want"
                                        " your character to be? "))

            print("Since you want your character to be",
                  character_level, "you have to multiply by 6000")
            print(character_level * 6000)
            print("The number above is the amount of mora needed"
                  " to get the character to that level")
        except ValueError:  # From live lesson
            print("Error...Only numbers")
            mora_calculator()
        user_choice_two = input("Enter 1 to end the program or"
                                " Enter 2 to continue it: ")
        if user_choice_two == 1:
            end_of_program()
        elif user_choice_two == 2:
            introduction()
        else:
            print("Error... try again")
            print("Only input numbers")
            mora_calculator()

    def end_of_program():
        """
        This is the function that will end my program and have some
        goodbyes
        :return:
        """
        print("Thank you for taking the time to run my program")
        print("Have a great day ^-^")

    def introduction():
        """
        This is just to fulfill some requirements that
        were not necessary in my program.
        :return:
        """
        # This is from geeksforgeeks
        print('02', '09', '2022', sep='-')
        print("Hello User,I hope this program will assist you in GI")
        # Genshin impact is a gacha game that has a system where you basically
        # have to spend money to be able to get the character you want
        # as it takes a lot of wishes
        print("Or Genshin Impact")
        print("Should you have any problems with please email "
              "the following email presented")
        print("Jaimeort", end='@')
        print("gmail.com")
        print("User, please input your name to start")
        name = input()
        print('Hello and hope you enjoy, ' + name)
        print("Now for some primogem stats")
        # What this numeric operator does is the exponent so it's
        # 4 to the tenth power
        print(4 ** 10)
        # The asterik multiplies and will be used to calculate
        print(9 * 11)
        # This numeric operator divides
        print(1600 / 100)
        # Modulus shows the remainder so 2 goes into 7 3 times with
        # a remainder of 1 so 1 will be the answer
        print(7 % 2)
        # This is the floor divison which rounds to the nearest whole number
        # when it divides
        print(14 // 3)
        # The adding will be edited in the future for collecting primogems
        print(160 + 20)
        # This numeric operator is the minus sign and works exactly the
        # same
        print(1600 - 160)
        # Below is the not equal operator
        number_x = 6
        number_y = 2
        print(number_x != number_y)
        # The not boolean operator example. Reference is w3schools
        example_of_not = False
        print(not example_of_not)
        # The or operator which only one conditions needs to be fulfilled
        # in order for it to go through
        example_of_or = (160 > 150 or 160 > 170)
        print(example_of_or)
        # The and boolean operator in which both sides must be true in order
        # for it to return a true otherwise it will be false.
        and_example = (6 > 2 and 6 < 12)
        print(and_example)
        # Prints congrats 5 times
        print("Congrats" * 5)
        print("Thank you for bearing with the statistics"
              "above")

    print("Program Loading......")
    loading_screen = 0
    # The while loop below will act as a loading screen by going
    # in increments of 10 from 0 to 100 like a loading screen takes
    # time to load.
    while loading_screen <= 100:
        if loading_screen % 1 == 0:
            print(loading_screen, end=" ")
            loading_screen += 10

    print("\n", "Welcome to my Integration project")
    choice = input("To begin, if you want to go to "
                   "calculate how much primogems needed to "
                   "wish for a character press 1,\n however press 2 "
                   "if you want to get the artifacts needed to \n "
                   "max out your character or press 3 for some statistics"
                   " for Genshin Impact Primogems: ")
    # This is where the user chooses what they want to do in the program
    # and it takes them to the part they want so if they choose the calculator
    # it will cause them to start the wish_total function
    if choice == "1":
        wish_total()

    elif choice == "2":
        mora_calculator()

    elif choice == "3":
        introduction()

    else:
        print("ERROR!! ERROR!!\n"
              "Try again and enter a number between 1 and 3")
        main()

    def five_star_characters(name):
        """
        This function is just to name some five star characters
        in genshin impact that I really like.
        :param name:
        :return:
        """
        print(name)
        five_star_characters("Mona")
        five_star_characters("Kazuha")
        five_star_characters("Jean")
        five_star_characters("Klee")
        five_star_characters("Lumine")


if __name__ == "__main__":
    main()
