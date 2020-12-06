import numpy as np

def print_header():
    print('\tWelcome to "Guess my number"!)
    print('\tThink of a number between 1 and 100 and I will guess it')  
    print('\tI will do thisin as few attemps as possible, Good luck! \n')      
          
def print_footer():
    print('I won! I will always beat you at this game!/n')

def valid_input():
    while True:
        reply = input("\nEnter 'low', 'high' or 'correct'.   ")
        if reply in ('low', 'high', 'correct'):
            return reply
        print("This is an invalid option")
          
          
def main():
          #print initial header and instructions
          print_header()
    #get the initial values for the program
          first_guess = np.random.randomint(low = 1, high = 101, size = 1)
          tries = 1
          low = 1
          high = 100
          
          print('if you are ready,'
                'Guess anything and we will start')
          input('/nenter anything and I will start')

    while True:
        guess = (low + high)//2
        print("I am guessing {}".format(guess))
        reply = valid_input()
        if reply == 'low':
            low = guess
        elif reply == 'high':
            high = guess
        else:
            print("Thank you for playing with me!")
            break

        if low == high:
            print("You cheated!")
            break

if __name__ == '__main__':
    main()
          
          
          
          
          
          
          
          
   
          
          
          
          