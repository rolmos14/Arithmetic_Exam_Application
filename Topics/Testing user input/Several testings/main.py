def check(number):
    try:
        number = float(number)
        number = int(number)
        if number >= 202:
            print(number)
        else:
            print("There are less than 202 apples! You cheated me!")
    except ValueError:
        print("It is not a number!")
