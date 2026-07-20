a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    z = a / int(b)
except TypeError as e:
    print("Type Error Exception")
    z = None
print(z)