import time

array_s = [i for i in range(2)]
array_m = [i for i in range(100)]
array_l = [i for i in range(100000)]


def boxes(array):
    t0 = time.time()
    print(array[0])
    print(array[1])
    t1 = time.time()
    print(f"Time taken: {t1 - t0} miliseconds")


boxes(array_s)
boxes(array_m)
boxes(array_l)