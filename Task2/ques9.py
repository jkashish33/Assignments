#Part 1:
# lucky_number = 9
# while True:
#     number = eval(input("Guess the lucky number:"))
#     if number == lucky_number:
#         break


#Part 2:
lucky_number = 9
while True:
    number = eval(input("Guess the lucky number:"))
    if number == lucky_number:
        break
    else:
        answer = input("Do you want to continue guessing? (yes/no): ")
        if answer == 'no':
            break