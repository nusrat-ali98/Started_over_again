file = "pi.txt"

with open(file) as f:
    lines = f.readlines()


pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

