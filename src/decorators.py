def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                with open(filename, "a") as file:
                    file.write(f"{func.__name__} ok\n")
                    print(result)
            except Exception as e:
                with open(filename, "a") as file:
                    file.write(f"{func.__name__}: {type(e).__name__}. Inputs {args}, {kwargs}")
                    print(f"{func.__name__}: {type(e).__name__}. Inputs {args}, {kwargs}")
            return result

        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

