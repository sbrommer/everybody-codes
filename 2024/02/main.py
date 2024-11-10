def parse_words(line):
    return line[6:].split(',')


def T(text):
    return [*map(''.join, zip(*text))]


def find(text, words, symbols=False, wrap=False):
    ix = set()

    for word in words:
        for r, line in enumerate(text):
            l = len(line)
            for c in range(l):
                line_ = (line * (wrap + 1))[c:]
                if line_.startswith(word):
                    ix |= {(r, (c+dc)%l)
                           for dc in range(1 if not symbols else len(word))}

    return ix


# Parse input
words, _, *text = [line.strip() for line in open(0).readlines()]
words = parse_words(words)

# Part 1
print('Part 1:', len(find(text, words)))

# Part 2
words += [word[::-1] for word in words]

print('Part 2:', len(find(text, words, True)))

# Part 3
ix = find(text, words, True, True) | \
     {(i, j) for j, i in find(T(text), words, True)}

print('Part 3:', len(ix))
