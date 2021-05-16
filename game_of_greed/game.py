from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        score=0
        dice_counter=Counter(dice_roll)
        for key in dice_counter:
            count = dice_counter[key]
            if count < 3:
                if key == 1:
                    score += 100
                elif key == 5:
                    score += 50
            else:
                if count >= 3:
                    score += key * 100
                    if key == 1:
                        score = 1000
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

            
