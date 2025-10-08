def add_number(num1, num2):


    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("please enter a number")
    else:
        print(num1 + num2)

print("Please enter two numbers")
print("if you want to quit program press 'Enter'")


while True:
    number1= input("enter a number: ")
    if number1 == "":
        break
    number2 = input("enter a second number: ")
    if number2 == "":
       break

    add_number(number1, number2)
