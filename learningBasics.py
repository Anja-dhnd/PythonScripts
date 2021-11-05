#Ex 1 variables

# name = input("What is your name? ")
# print("Hello " + name)
#
# birth_year = int(input("Enter your birth year= "))
# age = (2021 - birth_year)
# print(age)

#Ex 2 variables
# first = float(input("First= "))
# second = int(input("Second= "))
# print(first + second)

#Ex 3 methods

course = 'Python for beginners'
print(course.replace('for', '4'))
print('Python' in course)

#Ex 4 arithmetic

print(10**3) #10^3
print(10//3) # division with integer only

x = 10
x *= 3

#Ex 5 Logical Operators

price = 25
print(price > 10 and price < 30) # returns true if both are true

other_price = 5
print(not other_price > 10) # reverse any result

#Ex 6 if statements

temperature = 32

if temperature > 30:
    print("it's a hot day")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold.")
print('Done.')

#Ex 7

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))


