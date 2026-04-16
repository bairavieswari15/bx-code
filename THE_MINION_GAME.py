def minion_game(string):
    vowels = 'AEIOU'
    stuartscore = 0
    kevinscore = 0
    length = len(string)
    for i in range(length):
        score = length - i
        if string[i] in vowels:
            kevinscore += score
        else:
            stuartscore += score
    if stuartscore > kevinscore:
        print(f"Stuart {stuartscore}")
    elif kevinscore > stuartscore:
        print(f"Kevin {kevinscore}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)