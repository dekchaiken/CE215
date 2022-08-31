import binary_search as bs

sorted_sequence = (2, 5, 7, 9)
a = bs.search(sorted_sequence, 5)
print(a) # 1 - the index of the first element >= 5

b = bs.search(sorted_sequence, 6)
print(b) # 2 - the index of the first element >= 6 (element 2 with value 7)