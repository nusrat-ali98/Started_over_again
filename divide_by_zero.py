print("Enter two numbers for division")
print("If you want to exit then press 'q'")

while True:
    first_number = input("Enter first number: ")

    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(answer)
