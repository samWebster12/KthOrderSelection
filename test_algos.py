from typing import List
import numpy as np
import time
import random

#QuickSelect: Find i-th smallest element using quick select
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

#Median of medians: Find the i-th (1-n) largest
def mom(arr: List[int], i: int) -> int:
    k = 5

    if len(arr) < 3 * k:
        s_arr = sorted(arr)
        return s_arr[len(s_arr) - i]

    chunks = []
    for start in range(0, len(arr), k):
        chunks.append(arr[start : start + k])

    medians = []
    for c in chunks:
        c_sorted = sorted(c)
        median_idx = len(c_sorted) // 2
        medians.append(c_sorted[median_idx])


    med_of_med = mom(medians, len(medians) - (len(medians) // 2))

    L = []
    S = []
    for num in arr:
        if num > med_of_med:
            L.append(num)
        else:
            S.append(num)

    j = len(L)
    if j == i - 1:
        return med_of_med
    elif j > i - 1:
        return mom(L, i)
    else:
        return mom(S, i - j)

if __name__ == "__main__":
    i = 15

    hundred = 100
    thousand = 1000
    million = 1000000
    ten_million = 10000000
    fifty_million = 50000000
    hundred_million = 100000000
    two_hundred_million = 200000000
    billion = 1000000000

    arr = np.random.randint(1, hundred_million, hundred_million).tolist()
    
    mom_start = time.time()
    mom_res = mom(arr, i)
    mom_t = time.time() - mom_start

    sort_start = time.time()
    s_arr = sorted(arr)
    s_res = s_arr[len(s_arr) - i]
    sort_t = time.time() - sort_start

    select_start = time.time()
    sel_res = quickselect(arr, len(arr) - i)
    select_t = time.time() - select_start

    #print("Sorted array: ", s_arr)
    print(i, "th largest from mom: ", mom_res, "\t\tTime: ", mom_t)
    print(i, "th largest from sort: ", s_res, "\t\tTime: ", sort_t)
    print(i, "th largest from select: ", sel_res, "\t\tTime: ", select_t)
    print("MOM-Sort Ratio: ", mom_t / sort_t)