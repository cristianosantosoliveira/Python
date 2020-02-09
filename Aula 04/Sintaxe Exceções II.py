def ask():
    while True:
        try:
            n = int(input("Input a integer: "))
        except: 
            print("An erro ocorred! Please try again!")
            continue
        else:
            break

    print("Thank you, your number squared is: ", n**2)
ask()