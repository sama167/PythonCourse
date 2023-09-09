print("Welcome, please enter the step you want to hop")
step = int(input())

number = 0
game_over = False

while not game_over:
    number = number + 1
    print(f"number is {number}")
    if number % step == 0:         
        b = input()
        if b != "hop":
            print("error [1]")
            game_over = True

    else:
        b = input()
        if int(b) != number:
            print("error [2]")
            game_over = True