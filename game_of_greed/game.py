from collections import Counter
import random


class Game:
    round = 0
    avialable_dice = 6

    def __init__(self, roll=None):
        self.roll = roll or Game.roll_dice


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
        score = 0
        dice_counter = Counter(dice_roll)
        for key in dice_counter:
            count = dice_counter[key]

            if count < 2:
                if key == 1:

                    score = 100
                if key == 5:
                    score += 50

            elif count == 2:
                if key == 1:
                    score = 200
                if key == 5:
                    score += 100
            else:
                if count >= 3:
                    score += key * 100
                    if key == 1:
                        score = 1000
                    if key == 5:
                        score = 500
                        three_fivess = True
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

        if len(dice_counter) == 3 and not three_fivess:
            score = 1500

        return score

    def play(self):
        round = 0
        remaining_dice = 6

        print('Welcome to Game of Greed')
        user_input = input('(y)es to play or (n)o to decline\n>')

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
                print(f'*** {rolling_the_dice_result} ***')
                dice_input = input("Enter dice to keep, or (q)uit:")
                dice_input = dice_input.replace(' ','')
                # print(f'*** {dice_input}')

                fair_game = self.cheat(dice_input,dice_list)
                if dice_input =='q':
                    print(f"Total score is {banker_inc.balance} points\nThanks for playing. You earned {banker_inc.balance} points")
                    break

                else:
                     while not fair_game:
                        print('Cheater!!! Or possibly made a typo...')
                        print(f'*** {rolling_the_dice_result} ***')
                        dice_input = input("Enter dice to keep, or (q)uit:")
                        dice_input = dice_input.replace(' ','')
                        fair_game = self.cheat(dice_input, dice_list)
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
                     current_score = game_inc.calculate_score(tuple_for_input)
                     banker_inc.shelf(current_score)
                     print (f'You have {current_score} unbanked points and {remaining_dice} dice remaining')
                    



                     roll_or_bank = input('(r)oll again, (b)ank your points or (q)uit ')
                     if roll_or_bank == 'b':
                        print(f'You banked {banker_inc.bank()} points in round {round}')
                        print(f'Total score is {banker_inc.balance} points')
                        remaining_dice = 6


                    
                     elif roll_or_bank == 'q':
                        print(f"Total score is {banker_inc.balance} points")
                        print(f"Thanks for playing. You earned {banker_inc.balance} points")
                        break
                     elif roll_or_bank == 'r':
                   



        

    @staticmethod
    def cheat(dice_input,dice_list):

        a = Counter(dice_input).most_common()
        # print(a)
        b = Counter(dice_list).most_common()
        # print(b)
        if len(a) > len(b):
          return False
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


        return fair_game




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
test.play()
