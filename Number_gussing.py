win_num = 77
guess = 1

n = int(input("guess the number:"))

while True:

    if (win_num == n):
        print ("you won the game",guess)
        break

    elif (n < win_num):
        print("guess is low,type another number")

    else:
        print("guess is high,type another number")

    n = int(input("guess the number:"))
    guess = guess + 1