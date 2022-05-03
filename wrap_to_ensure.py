# Convert input to ensure it's printed in desired type
import functools


def ensure(*op):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            args = [i(j) for (i, j) in zip(op, args)]
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@ensure(int, float)
def tell_info(quantity, price):
    return f"The cost of {quantity} is ${price}"


print(tell_info(12, 13.49))
