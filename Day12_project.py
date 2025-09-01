try1="yes"
while try1=="yes":
    print("Welcome to the Number Guessing name Game!")
    print("I'm Guessing a  number between 1 and 100")
    level=input("Chose difficulty level, Type 'easy' or 'hard':")
    import random
    random_num=random.randint(1,100)
    def game(chances):
        print(f"You have {chances} attempts to guess the Number")
        end=False
        for a in range(1,chances+1):
            if end==False:
                num=int(input("Enter Number:"))
                if num>random_num:
                    print(f"Your choice is too high, attempt no:{a}")
                if num<random_num:
                    print(f"Your Choice is too low, attempt no:{a}")
                if num==random_num:
                    print("Congratulations You Win")
                    end=True
                    tryf="no"
        if end==False:
            tryf=input("You Lose\nDo you want to play again:")
            return tryf
    if level=="easy":
        try1=game(10)
    if level=="hard":
        try1=game(5)
     