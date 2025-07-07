def wrapper_function(original_function):
    def inner_function(*args, **kwargs):
        # Code to execute BEFORE the original_function
        print("Executing before the original function.")

        result = original_function(*args, **kwargs) # Call the original function

        # Code to execute AFTER the original_function
        print("Executing after the original function.")

        return result
    return inner_function

# Example usage with a decorator
@wrapper_function
def my_function(a, b):
    print(f"Inside my_function: {a} + {b} = {a + b}")
    return a + b

my_function(5, 3)