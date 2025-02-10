"""
This module demonstrates basic Python code structure and functions.
It includes examples of function definitions, variable usage, and basic logic.
"""

# Define the 'hello' variable
hello = "Hello"

def greet():
    """
    This function greets the user by attempting to print a variable.
    It has a bug where it tries to use an undefined variable 'hello'.
    """
    print(hello)  # Now 'hello' is defined

# Define the 'greet_user' function
def greet_user(name):
    """
    Function to greet the user by name.
    Args:
        name (str): The name of the user.
    """
    print(f"Hello, {name}!")

# Now call the function after it's defined
greet_user("Onyx")  # Function call to greet_user
