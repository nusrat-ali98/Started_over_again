def add_number(num1, num2):


    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("please enter a number")
    else:
        print(num1 + num2)


number1= input("enter a number: ")
number2 = input("enter a second number: ")
add_number(number1, number2)