from collections import Counter
import collections
import random


class Game:
    round = 0
    avialable_dice = 6

    def __init__(self, roll=None):
        self.roll = roll or Game.roll_dice
    @staticmethod
    def validate_keepers(dice_list, dice_input):
            # print("************" ,not Counter(dice_list) - Counter(dice_input))
            # return not Counter(dice_list) - Counter(dice_input)
        a = Counter(dice_input).most_common()
        # print(a)
        b = Counter(dice_list).most_common()
        # print(b)
        if len(a) > len(b):
          return True
        votes =0
        fair_game = False
        for i in a:
             for j in b:
                 if i[0] == j[0]:
                     if i[1] <= j[1]:
                          votes +=1
        if len(a) == votes:
            fair_game = True
        #    cheating =all([characters in b for characters in a])
        #    print(cheating)
        # print("*****" ,  fair_game)
        return fair_game
    

# Creating roll dice function


    def roll_dice(available_dice):
        # setup the rolls and giving them random numbers from 1 to 6
        counter = 0
        result = []
        while counter < available_dice:
            counter += 1
            result.append(random.randint(1, available_dice))

        # creating tuple
        roll_dice_tuple = tuple(result)
        return roll_dice_tuple

    @staticmethod
    def calculate_score(dice_roll):
        # (6, 6, 6, 1, 2, 1)
        # {"1":2, "2":1, "6":3}
        three_fivess = False
        pairs = 0
        score = 0
        dice_counter = Counter(dice_roll)
        for key in dice_counter:
            # print(key , "KEYYYYY")
            count = dice_counter[key]
            print(count , "COUNTTTT")

            if count < 2:
                if key == 1:
                    score += 100
                if key == 5:
                    score += 50

            elif count == 2:
                if key == 1:
                    score += 200
                if key == 5:
                    score += 100
            else:
                if count >= 3:
                    if key == 1:
                        score = 1000
                    elif key == 5:
                        score = 500
                        three_fivess = True
                    else:
                        score += key * 100


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
                if len(dice_counter) == 3 and not three_fivess:
                    score = 1500000

        if len(dice_counter) == 6:
            score = 1500

<<<<<<< HEAD
        for i in dice_counter:
            if dice_counter[i] == 2:
                pairs += 1
                if pairs == 3:
                    score = 0
                    score += 1500
                    return score
=======
        # if len(dice_counter) == 3 and not three_fivess:
        #     score = 1500000
>>>>>>> master

        return score
    @staticmethod
    def zilch_result(roll):
        x=Game.calculate_score(roll)
        if x==0:
            # zilch()
            print('****************************************\n**        Zilch!!! Round over         **\n****************************************')
            return True
        else:
            return False
    
    def filtering_testing(element):
        if element == 1 or element == 5:
            return True
        else:
            return False
        
        

    
    def get_scores(x):
        
        test_list = list(x)
        result_of_test_list = filter(Game.filtering_testing, test_list)
        result_t = tuple(result_of_test_list)
        return result_t



<<<<<<< HEAD
    def play(self):
        current_score = 0
=======
    def play(self, roller):
>>>>>>> master
        round = 0
        remaining_dice = 6

        print('Welcome to Game of Greed')
        user_input = input('(y)es to play or (n)o to decline\n> ')

        if user_input == 'n':
            print("OK. Maybe another time")
            exit()
        elif user_input == "y":
            game_inc = Game()
            banker_inc = Banker()
            while True:
                round += 1
                print(f"Starting round {round}\nRolling {remaining_dice} dice...")
                
                roll_result = self.roll(remaining_dice)
                dice_list = [str(i) for i in roll_result]
                rolling_the_dice_result = ' '.join([str(i) for i in roll_result])
                # rolling_the_dice_result = "1 2 5 1 2 1"
                print(f'*** {rolling_the_dice_result} ***')
                getScore= Game.zilch_result(roll_result)
                if getScore:
                    # print('zilch')
                    remaining_dice=6
                    continue

                dice_input = input("Enter dice to keep, or (q)uit:\n> ")

                dice_input = dice_input.replace(' ','')
                # print(f'*** {dice_input}')

                # fair_game = self.validate_keepers(dice_input,dice_list)
                if dice_input =='q':
                    print(f"Total score is {banker_inc.balance} points\nThanks for playing. You earned {banker_inc.balance} points")
                    break

                else:
                     while not Game.validate_keepers(dice_list, dice_input):

                        print('Cheater!!! Or possibly made a typo...')
                        print(f'*** {rolling_the_dice_result} ***')
                        dice_input = input("Enter dice to keep, or (q)uit:\n> ")
                        dice_input = dice_input.replace(' ','')
                        fair_game = self.validate_keepers(dice_input, dice_list)
                        getScore= Game.zilch_result(roll_result)
                        if getScore:
                            print('zilch')
                            remaining_dice=6
                            continue
                        if dice_input == 'q':
                            print(f"Total score is {banker_inc.balance} points\nThanks for playing. You earned {banker_inc.balance} points")
                            return
                                




                     tuple_for_input = tuple( int(num) for num in dice_input )
                     remaining_dice -=len(tuple_for_input)
                
                    # test_length = []
                    # for element in tuple_for_input:
                    #     if element in roll_result and element not in test_length:
                    #         test_length.append(element)
                    # if len(test_length) == len(tuple_for_input):
                     current_score += game_inc.calculate_score(tuple_for_input)
                     banker_inc.shelf(current_score)
                     print (f'You have {current_score} unbanked points and {remaining_dice} dice remaining')
                    



                     roll_or_bank = input('(r)oll again, (b)ank your points or (q)uit\n> ')
                     if roll_or_bank == 'b':
                        print(f'You banked {banker_inc.bank()} points in round {round}')
                        print(f'Total score is {banker_inc.balance} points')
                        remaining_dice = 6


                    
                     elif roll_or_bank == 'q':
                        print(f"Total score is {banker_inc.balance} points")
                        print(f"Thanks for playing. You earned {banker_inc.balance} points")
                        break
                     elif roll_or_bank == 'r':
                        pass
                   



        





# """
# Handle banking points
# Define a Banker class
# Add a shelf instance method
# Input to shelf is the amount of points (integer)

#  to add to shelf >>>add points to shelf .
# shelf should temporarily store unbanked points.
# Add a bank instance method
# bank should add any points on the shelf to total and reset shelf to 0.
# bank output should be the amount of points added to total from shelf.
# Add a clear_shelf instance method
# clear_shelf should remove all unbanked points.
# """


class Banker:


    def __init__(self):
        self.shelved=0
        self.balance=0
    


    #     assert banker.balance == 0
    # assert banker.shelved == 0
    # 

    def shelf(self,val: int):
        self.shelved+=val
 



    def bank(self):
        added_points = self.shelved
        self.balance += added_points
        self.shelved = 0
        return added_points




    def clear_shelf(self):
        self.shelved=0



# Game()
test = Game()
test.play(1)

# E         -*** 6 1 2 1 2 3 ***
# E         +*** 5 2 3 5 4 2 ***