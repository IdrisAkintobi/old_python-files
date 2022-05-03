# Decorator tell the number of times func is called
import functools


def repeat(_func=None, *, num_times=5):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            wrapper_repeat.count += 1
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        wrapper_repeat.count = 0
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat()
def say_hi(name):
    print(f"Hi {name}, my good friend")


say_hi('Adejare')
say_hi('Idris')
print(say_hi.count, f"{repeat.__name__!r}")


# import functools
# def singleton(cls):
#     """Make a class a Singleton class (only one instance)"""
#     @functools.wraps(cls)
#     def wrapper_singleton(*args, **kwargs):
#         if not wrapper_singleton.instance:
#             wrapper_singleton.instance = cls(*args, **kwargs)
#         return wrapper_singleton.instance
#     wrapper_singleton.instance = None
#     return wrapper_singleton


# @singleton
# class TheOne:
#     pass
