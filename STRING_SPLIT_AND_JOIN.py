def splitandjoin(line):
    words = line.split(" ")
    result = "-".join(words)
    return result
if __name__ == '__main__':
    line = input()
    result = splitandjoin(line)
    print(result)
