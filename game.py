from random import randint

guess = randint(1, 100)


def computer_guess(num):
    if guess > num:
        print('Too small')
        return main()
    elif guess < num:
        print('Too big')
        return main()
    else:
        return print('You guessed ' + str(guess) + ' and won')


def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num < 1 or num > 100:
                print("Must be in range [1, 100]")
            else:
                computer_guess(num)
        except ValueError:
            print("Please put in only whole numbers for example 4")


if __name__ == '__main__':
    main()
