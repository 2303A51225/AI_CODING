#generate python code for simple calculator  function

def calculator():
    print("Simple Calculator")
    print("Enter 'quit' to exit")

    while True:
        user_input = input("Enter an expression (e.g., 2 + 3): ")
        if user_input.lower() == 'quit':
            break

        try:
            result = eval(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")