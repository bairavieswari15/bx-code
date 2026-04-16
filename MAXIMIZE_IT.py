from itertools import product
k, m = map(int, input().split())
list_of_lists = []
for _ in range(k):
    row = list(map(int, input().split()))[1:]
    list_of_lists.append([x**2 for x in row])
max_value = 0
for combination in product(*list_of_lists):
    current_sum = sum(combination) % m
    if current_sum > max_value:
        max_value = current_sum
print(max_value)
