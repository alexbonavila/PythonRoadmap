from functools import wraps, partial


# Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# Decorator with Arguments
def decorator_with_args(number):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result * number

        return wrapper

    return my_decorator


@decorator_with_args(3)
def add(x, y):
    return x + y


# Using functools.wraps to Preserve Metadata
def my_decorator_with_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function."""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator_with_metadata
def say_hello_metadata(name):
    """A simple greeting function."""
    print(f"Hello {name}!")


# Class Decorator
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        result = self.func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result


@MyDecorator
def say_hello_class(name):
    print(f"Hello {name}!")


# Decorators with Optional Arguments
def my_decorator_optional(*decorator_args, **decorator_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator arguments:", decorator_args, decorator_kwargs)
            print("Function arguments:", args, kwargs)
            return func(*args, **kwargs)

        return wrapper

    if len(decorator_args) == 1 and callable(decorator_args[0]):
        return decorator(decorator_args[0])

    return decorator


@my_decorator_optional
def no_args_function():
    print("No arguments here.")


@my_decorator_optional(1, 2, three='four')
def args_function(x, y):
    print(f"Arguments in function: {x}, {y}")


# Running the functions to see the effects of decorators
if __name__ == "__main__":
    say_hello()
    print(add(2, 3))
    say_hello_metadata("Alice")
    print(say_hello_metadata.__name__)
    print(say_hello_metadata.__doc__)
    say_hello_class("Bob")
    no_args_function()
    args_function(3, 4)
