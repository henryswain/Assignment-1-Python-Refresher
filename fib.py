from functools import lru_cache
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished in {run_time:.8f} seconds: f({args[0]}) -> {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n -2)

if __name__ == "__main__":
    (fib(100))
