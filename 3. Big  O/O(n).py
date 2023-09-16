import time

array_s = ["nemo" for i in range(1)]
array_m = ["nemo" for i in range(100)]
array_l = ["nemo" for i in range(100000)]


def find_nemo(array):
    t0 = time.time()
    for i in array:
        if i == 'nemo':
            print("Found Nemo!")
    t1 = time.time()
    print(f"Time taken: {t1 - t0} miliseconds")


find_nemo(array_s)
find_nemo(array_m)
find_nemo(array_l)