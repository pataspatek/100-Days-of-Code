def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: #bugged version had 'or' instead of 'and'
            print("FizzBuzz")
        elif number % 3 == 0: #bugged version had 'if' instead of 'elif'
            print("Fizz")
        elif number % 5 == 0: #bugged version had 'if' instead of 'elif'
            print("Buzz")
        else:
            print(number) #bugged version had a square brackets around the 'number'


def leap_year():
    year = int(input("Which year do you want to check?")) #bugged version had this input in a form of a string, not integer

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")
  

def odd_even():
    number = int(input("Which number do you want to check?"))

    if number % 2 == 0: #bugged version had only one equal sign
        print("This is an even number.")
    else:
        print("This is an odd number.")
    
