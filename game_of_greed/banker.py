"""Handle banking points
Define a Banker class
Add a shelf instance method
Input to shelf is the amount of points (integer)

 to add to shelf >>>add points to shelf .
shelf should temporarily store unbanked points.
Add a bank instance method
bank should add any points on the shelf to total and reset shelf to 0.
bank output should be the amount of points added to total from shelf.
Add a clear_shelf instance method
clear_shelf should remove all unbanked points.
"""


class Banker:


    def __init__(self):
        self.shelved=0
        self.balance=0
    


    #     assert banker.balance == 0
    # assert banker.shelved == 0
    # 

    def shelf(self,val):
        self.shelved+=val
 



    def bank(self,val):
        self.balance+=val
        self.clear_shelf()




    def clear_shelf(self):
        self.shelved=0



