
import random
name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
raise_per = (random.randint(1, 100))
raise_amount = (raise_per / 100) * salary + salary
print(name + ", your current salary is $" + str(salary))
print("Your raise is %" + str(raise_per))
print(name + ", your new salary is $" + str(raise_amount))