# STONE PAPER  SCISSOR GAME

#importing random module
import random
def game(computer,you):
    #Game rules
    if computer==you:
        print("same pick")
        return None
    elif computer=='s':
        if you=='sc':
            print("reason:bcz computer's stone broke ur scisssor")    #reason why who won
            return False
        elif you=='p':
            print("reason: bcz ur paper grabbed computer's stone")
            return True      
    elif computer == 'p':
        if you=='sc':
            print("reason:bcz ur scissor cut computer's paper have torn")
            return True
        elif you=='s':
            pront("reason: bcz computer's paper grabbed ur stone")
            return False 
    elif computer=='sc':
        if you=='s':
            print("reason:bcz ur stone broke compter's  scissor")
            return True
        elif you=='p':
            print("reason:bcz compter's scissor cut ur paper")
            return False                   
print('''computer's choice:- stone(s) or paper(p) or scissor(sc)''')
#rand int  functin use                           
random_no=random.randint(1,3)
if  random_no==1:
    computer='s'
elif random_no==2:
    computer='p'   
elif random_no==3:
    computer='sc'    
you=input('''computer's choice:- stone(s) or paper(p) or scissor(sc)
                               choose:-''')
a=game(computer,you)
# to know pickings
print(computer)
print(you)
# to declare result
if a==None:
    print("oops! the game is tie")
elif(a):
    print("you win")
else:
    print("you loose.")    