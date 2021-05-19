  
from collections import Counter
import random


class Game:
    round = 1
    avialable_dice = 6

    def __init__(self, roll=None):
        self.roll = roll or Game.roll_dice
   

    @staticmethod
    def validate_keepers(dice_list, dice_input):
        a = Counter(dice_input).most_common()
        b = Counter(dice_list).most_common()
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

    # @staticmethod
    # def calculate_score(dice_roll):
    #     # (6, 6, 6, 1, 2, 1)
    #     # {"1":2, "2":1, "6":3}
    #     three_fivess = False
    #     pairs = 0
    #     score = 0
    #     dice_counter = Counter(dice_roll)
    #     for key in dice_counter:
    #         # print(key , "KEYYYYY")
    #         count = dice_counter[key]

    #         if count < 2:
    #             if key == 1:
    #                 score += 100
    #             if key == 5:
    #                 score += 50

    #         elif count == 2:
    #             if key == 1:
    #                 score += 200
    #             if key == 5:
    #                 score += 100
    #         else:
    #             if count >= 3:
    #                 if key == 1:
    #                     score = 1000
    #                 elif key == 5:
    #                     score = 500
    #                     three_fivess = True
    #                 else:
    #                     score += key * 100


    #             if count >= 4:
    #                 if key == 1:
    #                     score += 1000
    #                 else:
    #                     score += key * 100
    #             if count >= 5:
    #                 if key == 1:
    #                     score += 1000
    #                 else:
    #                     score += key * 100

    #             if count == 6:
    #                 if key == 1:
    #                     score += 1000
    #                 else:
    #                     score += key * 100
    #             if len(dice_counter) == 3 and not three_fivess:
    #                 score = 1500000

    #     if len(dice_counter) == 6:
    #         score = 1500

    #     for i in dice_counter:
    #         if dice_counter[i] == 2:
    #             pairs += 1
    #             if pairs == 3:
    #                 score = 0
    #                 score += 1500
    #                 return score

    #     return score

    @staticmethod
    def calculate_score(dice_roll):

        score = 0
        counter = 0

        dice_roll_counter_dict = Counter(dice_roll)

        for i in range(1, 7):
            if dice_roll_counter_dict[i] == 1:
                counter += 1
            if dice_roll_counter_dict[i] == 2:
                counter += 3

        if counter == 6 or counter == 9:
            score = 1500
            return score

        for key in dice_roll_counter_dict:

            if dice_roll_counter_dict[key] > 2:
                if key == 1:
                    score += (dice_roll_counter_dict[key]-2) * key * 1000

                else:
                    score += (dice_roll_counter_dict[key]-2) * key * 100

            elif key == 5:
                score += dice_roll_counter_dict[key] * 50

            elif key == 1:
                score += dice_roll_counter_dict[key] * 100

        return score

    


    @staticmethod
    def get_scorers(dice_roll):

        dice_roll_dict = Counter(dice_roll)

        results = []
        counter = 0
        
        for i in range(1, 7):
            if dice_roll_dict[i] == 1:
                counter += 1
            if dice_roll_dict[i] == 2:
                counter += 3

        if counter == 6 or counter == 9:
            return dice_roll

        for key in dice_roll_dict:
            if key == 1 or key == 5:
                for i in range(dice_roll_dict[key]):
                    results.append(key)

            elif dice_roll_dict[key] >= 3:
                for i in range(dice_roll_dict[key]):
                    results.append(key)
        
        return tuple(results)
                



    @staticmethod
    def zilch_result(roll):
        x=Game.calculate_score(roll)
        if x==0:
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


    @classmethod
    def play(cls, roller=None):
        roller = roller or Game.roll_dice
        current_score = 0
        round = 0
        remaining_dice = 6
        skip_roll = False
        cheater = False

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        user_input = input("> ")

        if user_input == 'n':
            print("OK. Maybe another time")
            exit()

        elif user_input == "y":
            game_inc = Game()
            banker_inc = Banker()
            while banker_inc.balance <= 10000:

                if not skip_roll and not cheater:
                    round += 1
                    remaining_dice = 6
                    print(f"Starting round {round}")

                

                if not cheater:
                    print(f"Rolling {remaining_dice} dice...")
                    roll_result = roller(remaining_dice)
                    dice_list = [str(i) for i in roll_result]

                    rolling_the_dice_result = ' '.join(map(str, roll_result))



                zilcher = game_inc.calculate_score(roll_result)
                
                print(f'*** {rolling_the_dice_result} ***')

                if zilcher == 0:
                    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
                    
                    print(f'You banked 0 points in round {round}')

                    print(f'Total score is {banker_inc.balance} points')

                    skip_roll = False

                    continue
                
                
                print("Enter dice to keep, or (q)uit:")

                dice_input = input("> ").replace(' ', '')
                
                if dice_input =='q':
                    print(f"Thanks for playing. You earned {banker_inc.balance} points")
                    break

                elif not dice_input.isdigit():
                    print(f"Thanks for playing. You earned {banker_inc.balance} points")
                    break

                else:
                    dice_to_keep_tuple = tuple(int(num)for num in dice_input)

                    cheater = not game_inc.validate_keepers(roll_result,dice_to_keep_tuple)

                    if cheater :
                        print('Cheater!!! Or possibly made a typo...')
                        continue

                    current_score = game_inc.calculate_score(dice_to_keep_tuple)
                    banker_inc.shelf(current_score)

                    remaining_dice = remaining_dice - len(dice_to_keep_tuple)
                    print(f'You have {banker_inc.shelved} unbanked points and {remaining_dice} dice remaining')

                    

                    print("(r)oll again, (b)ank your points or (q)uit:")

                    roll_or_bank = input("> ")

                    if roll_or_bank == 'b':
                        skip_roll = False
                        print(f'You banked {banker_inc.bank()} points in round {round}')
                        print(f'Total score is {banker_inc.balance} points')

                    elif roll_or_bank == 'q':
                        print(f"Thanks for playing. You earned {banker_inc.balance} points")
                        break

                    elif roll_or_bank == 'r' and remaining_dice != 0:
                        skip_roll = True
                        

            else:
                print(f"Thanks for playing. You earned {banker_inc.balance} points")

class Banker:


    def __init__(self):
        self.shelved=0
        self.balance=0
    
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
# test = Game()
# test.play()