m_size = input()
m_set = set(map(int, input().split()))
n_size = input()
n_set = set(map(int, input().split()))
sym_diff = m_set.symmetric_difference(n_set)
result = sorted(sym_diff)
for val in result:
    print(val)
