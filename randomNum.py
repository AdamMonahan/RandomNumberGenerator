import random

def randomNum():

    print("Hello, and welcome to the random number generator!")

    while True:

        num1 = int(input('Please enter your lower threshold: '))
        num2 = int(input('Please enter your upper threshold: '))

        def generate(num1, num2):
            return (random.randint(num1, num2))

        print(f'Your random number is {generate(num1, num2)}')

        again = input("Would you like to get another number? ")

        if not again.lower() in {'y', 'yes'}:
            print("Goodbye!")
            return



randomNum()