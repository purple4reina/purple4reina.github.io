import sys

for fname in sys.argv[1:]:
    top = []
    bottom = []
    with open(fname) as f:
        top.append(f.readline())
        top.append(f.readline())
        date = f.readline()[11:]
        for l in f:
            bottom.append(l)

    try:
        better_date = '%d-%s-%s' % (int(date[6:-1]), date[:2], date[3:5])
    except ValueError:
        print('fname: ', fname)
        continue

    with open(fname, 'w') as f:
        for l in top:
            f.write(l)

        f.write('completed: ')
        f.write(better_date)
        f.write('\n')

        for l in bottom:
            f.write(l)
