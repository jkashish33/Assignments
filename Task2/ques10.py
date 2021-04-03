lucky_number = 9
counter = 5
while counter > 0:
    number = eval(input("Guess the lucky number:"))
    if number == lucky_number:
        print("Good Guess!")
        break
    else:
        if counter > 1:
            print("Try again!")
        counter -= 1
if counter == 0:
    print("Game Over!")