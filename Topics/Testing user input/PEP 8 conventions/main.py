def check_name(variable):
    if variable in ["l", "O", 'I']:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif variable.islower():
        print("It is a common variable")
    elif variable.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
