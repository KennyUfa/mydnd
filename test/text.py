import threading
import time


def print_fib(b) -> None:
    def fib(b) -> int:
        if b == 1:
            return 0
        elif b == 2:
            return 1
        else:
            return fib(b - 1) + fib(b - 2)

    print(f'fib({b}) равно {fib(b)}')


def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()

start_threads = time.time()
fibs_with_threads()
end_threads = time.time()
print(f'Многопоточное вычисление заняло {end_threads - start_threads:.4f} с.')
