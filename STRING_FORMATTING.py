def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hex_val = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{dec} {octal} {hex_val} {binary}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)