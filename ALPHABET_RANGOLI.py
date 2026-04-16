def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for i in range(size):
        left = list(alpha[size-1:size-i-1:-1])
        right = list(alpha[size-i-1:size])
        row = "-".join(left + right)
        lines.append(row.center(4*size-3, "-"))
    print('\n'.join(lines[:-1] + lines[::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)