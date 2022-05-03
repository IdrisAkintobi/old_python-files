from functools import wraps
from time import perf_counter as pf
from math import factorial
def debug(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		arguments = [str(i) for i in args]
		k_arguments = [f"{x}={j}" for x,j in kwargs.items()]
		all_args = ", ".join(arguments+k_arguments)
		start_time = pf()
		fn(*args, **kwargs)
		end_time = pf() - start_time
		return f"The signatures of the function {fn.__name__} are {all_args}\
		and the time taken for the function to run is {end_time:.2f}secs"
	return wrapper

@debug
def waste_time():
	x = iter(map(lambda X: factorial(X), range(20,6200)))
	return sum([i*2 for i in x])
print(waste_time())
