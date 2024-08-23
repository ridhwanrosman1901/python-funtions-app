# Greeting the user
def greet_user(name):
    print(f"Hello {name}, welcome to my app.")
name = input("What is your name? ")
greet_user(name)

# App calculate User's age
a = int(input("How old are you? "))
b = 5
sum_numbers = a + b
print(f"So in the next 5 years, you will be {sum_numbers} years old.")

# List of fruits
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")
fruits.remove("banana")
fruits.insert(1, "blueberry")
fruits.sort()

print("Here's a list of fruits sorted alphabetically:")
print(fruits)

# Loop 1-10 then break
print("Select a number 1-10 that you love")
love = int(input("Enter a number: "))
for i in range(1, 11):
    if i == love:
        print(i)
        print("I've count until we reached the number that you love.")
        break
    print(i)

# Loop 1-10 then skip
print("Next, select a number (1-10) that you hate.")
hate = int(input("Enter a number: "))
for i in range(1, 11):
    if i % hate == 0:
        continue
    print(i)
print("Here, I've deleted the number that you hate. :)")

print("That's all for today, come again later!")