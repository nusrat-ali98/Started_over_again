def t_shirt(size, message):
    print("Size of shirt is "+ size + " and message is "+ message)


shirt_size = input("choose your  shirt size 's','m','l'> ")
shirt_message = input("write a message that you want to print ")
if shirt_size == "l" or shirt_size == "m" :
    t_shirt(shirt_size, message = 'I love python')
else:
    t_shirt(shirt_size, message = shirt_message)

