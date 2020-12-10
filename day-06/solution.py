from collections import Counter

def part1(groups):
    res = 0

    for g in groups:
        yes = set()
        for question in g:
            if question != "\n":
                yes.add(question)

        res += len(yes)

    return res

def part2(groups):
    res = 0

    for g in groups:
        questions = g.split("\n")
        if questions[-1] == '':
            questions.pop()

        population = len(questions)
        counts = Counter(g)

        for q in counts:
            res += counts[q] == population and q != "\n"

    return res

with open('input-01.txt') as f:
    groups = f.read().split("\n\n")
    print(part1(groups),part2(groups))