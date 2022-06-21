import random;

number= random.randint(0, 19)
chances= 0;

while chances <=5:
    guess= int(input("Enter your number: "));

    if guess == number:
        print("CONGRATULATIONS, YOU WON!!");
        break;

    elif guess> number:
        print("Hint: The number you chose was too high")

    else:
        print("Hint: The number you chose was too low")

    #guess= int(input("Enter your number: "));
    chances= chances + 1;  

if not chances <= 5:
    print("You lose, the number is ", number);