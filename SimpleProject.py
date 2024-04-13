def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero")
        return None

def main():
    print("Welcome to Simple Calculator!")
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print("Result: ", result)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
