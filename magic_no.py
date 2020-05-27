import random
def magic_num():
    magic_num=random.randint(0,11)
    num=input("Enter num between 1 to 10:")
    if int(num)==magic_num:
        print("you've won the game!!")
    else:
        print("play again ")
    print("Magic Number is {} ".format(magic_num))
magic_num()