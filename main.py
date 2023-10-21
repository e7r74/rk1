
name = input("Please enter your name: ")

salary = input("Please enter your desired level of salary: ")

try:
    salary = float(salary)
except ValueError:

    print("Invalid input. Please enter a numeric value for salary.")
    exit()
tax_level = salary * 0.2
print(f"Hello, {name}. Your desired level of salary is {salary:.2f} and your tax level to pay is {tax_level:.2f}.")




#Using arithmetic,bitwise and logic ops

add = lambda x, y: x + y
mul = lambda x, y: x * y
div = lambda x, y: x / y
exp = lambda x, y: x ** y

operations = {1: add, 2: mul, 3: div, 4: exp}


print("Choose an operation:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

choice = int(input("Enter your choice (1/2/3/4): "))


if choice in operations:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    result = operations[choice](num1, num2)
    print(f"The result is {result}")
else:

    print("Invalid choice")




#Loops and iterations

def fibonacci(n):

  f1 = 1
  f2 = 1

  sequence = []

  for i in range(n):

    sequence.append(f1)

    c = f1 + f2

    f1 = f2
    f2 = c

  return sequence

n = int(input("Enter the length of the Fibonacci sequence: "))

print(fibonacci(n))





# Tuples and sets

def store_items(items):

  items = [item.strip() for item in items.split(",")]

  unique = set()

  frequency = {}

  for item in items:

    if item in unique:

      frequency[item] = frequency.get(item, 0) + 1

    else:

      unique.add(item)

  non_unique = []

  for item, count in frequency.items():

    non_unique.append((item, count))

  non_unique = tuple(non_unique)

  return (unique, non_unique)

items = input("Enter the items separated by comma: ")

print(store_items(items))



#list and dictionries

def todo_list():

  tasks = []

  while True:

    print("What do you want to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

      task = input("Enter a task: ")

      tasks.append((task, "pending"))

      print(f"Task '{task}' added successfully.")

    elif choice == "2":

      if not tasks:

        print("You have no tasks.")
      else:

        print("Your tasks are:")

        for i, (task, status) in enumerate(tasks, 1):
          print(f"{i}. {task} - {status}")

    elif choice == "3":

      if not tasks:

        print("You have no tasks.")
      else:

        print("Your tasks are:")

        for i, (task, status) in enumerate(tasks, 1):
          print(f"{i}. {task} - {status}")

        number = int(input("Enter the number of the task to mark as completed: "))

        if number < 1 or number > len(tasks):

          print("Invalid number.")
        else:

          task, status = tasks[number - 1]

          if status == "completed":

            print(f"Task '{task}' is already completed.")
          else:

            tasks[number - 1] = (task, "completed")

            print(f"Task '{task}' marked as completed.")

    elif choice == "4":

      print("Goodbye!")

      break

    else:
      print("Invalid choice.")

    print()

todo_list()


