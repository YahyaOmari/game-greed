from collections import Counter
import random

class GameLogic:
# Creating roll dice function
    def roll_dice():
        # setup the rolls and giving them random numbers from 1 to 6 
        first_roll =  random.randint(1,6)
        second_roll = random.randint(1,6)
        third_roll = random.randint(1,6)
        fourth_roll = random.randint(1,6)
        fifth_roll = random.randint(1,6)
        sixth_roll = random.randint(1,6)

        # creating tuple 
        roll_dice_tuple = ()

        # since tuple is a immutable object so I want to convert tuple to list
        # by built in function list() so I can append anything to the list
        roll_dice_list = list(roll_dice_tuple)

        # so now we can append to the list 
        roll_dice_list.append(first_roll)
        roll_dice_list.append(second_roll)
        roll_dice_list.append(third_roll)
        roll_dice_list.append(fourth_roll)
        roll_dice_list.append(fifth_roll)
        roll_dice_list.append(sixth_roll)

        # now we are using another built in function tuple() to convert this list back to tuple
        roll_dice_tuple =  tuple(roll_dice_list)

        return roll_dice_tuple
        # print(roll_dice_tuple)

    @staticmethod
    def calculate_score(dice_roll):
        # (6, 6, 6, 1, 2, 1)
        # {"1":2, "2":1, "6":3}
        three_fivess=False
        score=0
        dice_counter=Counter(dice_roll)
        for key in dice_counter:
            count = dice_counter[key]
            
            if count<2:
                if key==1:

                    score=100
                if key==5:
                    score+=50
                
            elif count == 2 :
                if key == 1:
                    score = 200
                if key == 5:
                    score +=100
            else:
                if count >= 3:
                    score += key * 100
                    if key == 1:
                        score = 1000
                    if key== 5 :
                        score=500
                        three_fivess=True
                if count >= 4:
                    if key == 1:
                        score += 1000
                    else:
                        score += key * 100
                if count >= 5:
                    if key == 1:
                        score += 1000
                    else:
                        score += key * 100

                if count == 6:
                    if key == 1:
                        score += 1000
                    else:
                        score += key * 100



        if len(dice_counter) == 6:
            score = 1500



        if len(dice_counter)  == 3 and not three_fivess :
            score = 1500

        return score


    def welcome_function():
        round = 0

        print('Welcome to Game of Greed')
        user_input = input('Wanna play?')

        if user_input == 'n':
            print("OK. Maybe another time")
            exit()
        elif user_input == "y":
            round +=1 
            print(f"Starting round {round} \nRolling 6 dice...")
            
            # GameLogic.roll_set()
            rolling_the_dice_result = GameLogic.roll_dice()
            print(rolling_the_dice_result)

            GameLogic.roll_set(rolling_the_dice_result)
            return rolling_the_dice_result

    def roll_set(result):

        user_dice_input = input("Enter dice to keep (no spaces), or (q)uit: ")
        
        if user_dice_input =='q':
            exit()


        integer_to_list = [int(d) for d in str(user_dice_input)]

        for i in integer_to_list:
            if i  in result:
                print(integer_to_list)
                list_to_tuple_for_input = tuple(integer_to_list)
                # print(list_to_tuple_for_input)
                calculating_score = GameLogic.calculate_score(list_to_tuple_for_input)
                print(f"Total score is {calculating_score} points")
            else:
                print("Cheater!! Or possibly made a typo...")
                GameLogic.roll_set(result)
        

GameLogic.welcome_function()
# GameLogic.roll_set()







    #    if user_dice_input == "q":
    #         exit()
    #     else:
    #         integer_to_list = [int(d) for d in str(user_dice_input)]
    #         # print(integer_to_list)

    #         if  not  range(1,7)  in integer_to_list :
    #             print("Cheater!! Or possibly made a typo...")
                
    #             # GameLogic.roll_set()
    #         elif range(1,7)  in integer_to_list:
    #             list_to_tuple_for_input = tuple(integer_to_list)
    #             calculating_score = GameLogic.calculate_score(list_to_tuple_for_input)
    #             print(f"Total score is {calculating_score} points")