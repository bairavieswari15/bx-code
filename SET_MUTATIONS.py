import sys

if __name__ == '__main__':
    input_data = sys.stdin.read().split() 
    if not input_data:
        sys.exit()
    ptr = 0
    n_a = int(input_data[ptr])
    ptr += 1
    set_a = set(map(int, input_data[ptr:ptr + n_a]))
    ptr += n_a
    n_ops = int(input_data[ptr])
    ptr += 1
    for _ in range(n_ops):
        operation = input_data[ptr]
        other_set_len = int(input_data[ptr + 1])
        ptr += 2
        other_set = set(map(int, input_data[ptr:ptr + other_set_len]))
        ptr += other_set_len
        if operation == "update":
            set_a.update(other_set)
        elif operation == "intersection_update":
            set_a.intersection_update(other_set)
        elif operation == "difference_update":
            set_a.difference_update(other_set)
        elif operation == "symmetric_difference_update":
            set_a.symmetric_difference_update(other_set)
    print(sum(set_a))
