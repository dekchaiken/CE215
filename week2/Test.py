import binary_search as bs
import linear_search
import random
import time
my_list = [1, 3, 5, 7 ,9]
#print(binary_search.binary(my_list, 3))
#print(binary_search.binary(my_list, -1))
#print(linear_search.linear(my_list, 3))
#print(linear_search.linear(my_list, -1))


size_list = [1000,10000,100000,1000000,10000000]
result_list_binary = []
result_list_linear = []
for size in size_list:
    print(f"The size is {size}")
    new_list = set([])
    while len(new_list) < size:
        new_list.add(random.randint(1, 10*size))
    new_list.add(10000000)
    new_list = list(new_list)
    new_list = sorted(new_list)
    #print(new_list)
    binary_start_time = time.perf_counter()
    binary_result = binary_search.binary(new_list, 10000000)
    print(f"Binary search takes {time.perf_counter() -binary_start_time} seconds.")
    print(binary_result)
    result_list_binary.append(time.perf_counter() -binary_start_time)
    linear_start_time = time.perf_counter()
    linear_result = linear_search.linear(new_list, 10000000)
    print(f"Linear search takes {time.perf_counter() -linear_start_time} seconds.")
    print(linear_result )
    result_list_linear.append(time.perf_counter() -linear_start_time)