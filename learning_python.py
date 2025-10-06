file_name = "python_learning"
with open(file_name) as f:
    print(f.read())




with open(file_name) as file:
     for line in file:
        print(line.rstrip())

with open(file_name)as f:
    lines = f.readlines()

    for line in lines:
        new_line = line.replace('python','snake')
        print(new_line.rstrip())