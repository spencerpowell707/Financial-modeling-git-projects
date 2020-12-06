def main():
    low = 0
    high = 101

    print("Think of a number between 1 and 100")

    print("When you are ready,"
          " let me know and I will attempt to guess your number.")
    input("\nEnter anything and I will begin: ")

    def valid_input():
        while True:
            reply = input("\nEnter 'low', 'high' or 'correct'.   ")
            if reply in ('low', 'high', 'correct'):
                return reply
            print("I do not understand what you wrote.")

    while True:
        guess = (low + high)//2
        print("I am guessing {}".format(guess))
        reply = valid_input()
        if reply == 'low':
            low = guess
        elif reply == 'high':
            high = guess
        else:
            print("Thank you for playing!")
            break

        if low == high:
            print("Impossible!")
            break

if __name__ == '__main__':
    main()