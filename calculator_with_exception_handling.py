import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def display_menu():
    print("What do you want to do with the numbers? ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


print("Welcome to the calculator.")
while True:
    try:
        num_one = int(input("Enter a number: "))
        num_two = int(input("Enter another number: "))
    except ValueError:
        logging.exception("An exception occurred: ValueError")
        print("Invalid input! Please enter a valid number.")
    else:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            answer = num_one + num_two
            print(f'{num_one} + {num_two} = {answer}')
        elif choice == "2":
            answer = num_one - num_two
            print(f'{num_one} - {num_two} = {answer}')
        elif choice == "3":
            answer = num_one * num_two
            print(f'{num_one} * {num_two} = {answer}')
        elif choice == "4":
            try:
                answer = num_one / num_two
            except ZeroDivisionError:
                logging.exception("An exception occurred: division by zero")
                print("You can't divide by zero.")
            else:
                print(f'{num_one} / {num_two} = {answer}')
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
