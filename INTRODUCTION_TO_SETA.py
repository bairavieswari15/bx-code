def average(array):
    distinct_heights = set(array)
    total_sum = sum(distinct_heights)
    count = len(distinct_heights)
    return total_sum / count
