import random

class GameLogic:
    pass

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

Testing = GameLogic

print(Testing.roll_dice())