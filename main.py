"""Integration project: Genshin Impact Wish calculator"""
# This program in the end will hopefully be a way to tell how you will
# a certain charater in genshin impact.


def main():
    """
    This is the main function that will run my program
    :return:
    """

    def daily_commisons():
        """
        This function serves to calculate the primogems from daily
        commissions.It will ask the user to input how many they
        complete and calculate it and total it.
        :return:
        """
        primogems_daily = int(input("How many daily commissions did you do? "))
        primogems_awarded = 40
        primogems_earned = primogems_daily * primogems_awarded
        print("You earned ", primogems_earned, "primogems")
        print()

    def storyline_primo():
        """
        This function serves to calculate the amount earned from completing
        the storylines in the game.The user gets 60 primogems per
        quest so in this function we get how many storylines
        they did multiplied by 60.
        :return:
        """
        primogems_storyline = int(input("How many storylines"
                                        " did you complete? "))
        primogems_storyline_awarded = 60
        primogems_storyline_earned = \
            primogems_storyline * primogems_storyline_awarded
        print("You earned", primogems_storyline_earned, "primogems")
        print()

    def farming_for_primogems():
        """
        This function serves to calculate the amount made from farming.

        :return:
        """
        primogems_farming = int(
            input("How many small quests did you complete? "))
        primogems_farming_awarded = 5
        primogems_farming_earned = \
            primogems_farming * primogems_farming_awarded
        print("You earned", primogems_farming_earned, "primogems")

    def wish_total():
        """
        This functions serves to add the grand totals of
        the other function to add them to see how much
        wishes they can get.
        :return:
        """
        farming_for_primogems()
        daily_commisons()
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
        # From pynative.com
        wishing_banner_list = ['Rust', 'The Flute', 'The Widsith',
                               'Sacrificial Greatsword', 'Razor',
                               'Bennet', 'Mona', 'Kazuha', 'Jean']
        total_wishes = int(input("How much wishes do you have?"))
        for x in range(total_wishes):
            wishing = random.choice(wishing_banner_list)
            print(wishing)
        print("Would you like to keep going or end the program?")
        user_choice = input("Enter 1 to end the program or"
                            " Enter 2 to continue it")
        if user_choice == 1:
            end_of_program()
        else:
            mora_calculator()

    def mora_calculator():
        """
        This function asks user for what level do they want to upgrade
        their character too.Each level cost 6000 mora so
        all you have to do is multiply the level you want by 6000.Mora
        is the in game currency.
        :return:
        """
        print("In Genshin Impact you need mora in order to"
              " upgrade a character \nand it goes by levels of "
              "1")
        character_level = int(input("What level do you want"
                                    " your character to be? "))

        print("Since you want your character to be",
              character_level, "you have to multiply by 6000")
        print(character_level * 6000)
        print("The number above is the amount of mora needed"
              " to get the character to that level")

        user_choice_two = input("Enter 1 to end the program or"
                                " Enter 2 to continue it: ")
        if user_choice_two == 1:
            end_of_program()
        elif user_choice_two == 2:
            introduction()
        else:
            print("Error... try again")
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
        This is just to fufill some requirements that
        were not necessary in my program.
        :return:
        """
        # This is from geeksforgeeks
        print('02', '09', '2022', sep='-')
        print("Hello User,I hope this program will assist you in GI")
        # Genshin impact is a gacha game that has a system where you basically
        # have to
        # Spend money to be able to get the character you want as it takes
        # a lot of wishes
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
        # What this does is print congrats 5 times
        number_x = 6
        number_y = 2
        print(number_x != number_y)
        example_of_not = False
        print(not example_of_not)
        example_of_or = (160 > 150 or 160 > 170)
        print(example_of_or)
        and_example = (6 > 2 and 6 < 12)
        print(and_example)
        print("Congrats" * 5)

    print("Program Loading......")
    loading_screen = 0
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
