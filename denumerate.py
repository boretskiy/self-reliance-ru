import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as in_, open(sys.argv[2], 'w') as out:
        paragraph = []
        text = []
        for line in in_.readlines():
            line = line.strip()
            if line:
                paragraph.append(line.split(' ', 1)[1])
            else:
                text.append(' '.join(paragraph))
                paragraph = []
        text.append(' '.join(paragraph))
        out.write('\n'.join(text))

