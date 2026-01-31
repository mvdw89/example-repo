# Initiate the number variable
# Initiate the number_list list variable (empty)

number = 0
number_list = []

# Print instructions

print("Program to aggregate and average numbers")
print("")
print("0 will be accepted, but omitted from the calculation")
print("Enter -1 to exit the program")
print("")

# Initiate while loop to collect valid numbers
# Loop will terminate when -1 is input via boolean

while number != (-1):
    if number != 0:
        number_list.append(number)

    number = float(input("Enter a number: "))

number_average = sum(number_list) / len(number_list)

print("")
print("The list of valid numbers are:   {}".format(number_list))
print("")
print("THe average of valid numbers:    {}".format(number_average))
print("")