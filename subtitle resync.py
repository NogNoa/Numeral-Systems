import argparse
from ntpath import basename
from codecs import open
from TimeCode import TimeCode

parser = argparse.ArgumentParser()
parser.add_argument('srt', help='path to subtitle file to be resynced')
parser.add_argument('fix', help="time difference in format h:m:s,ms. Minus sign to make the fix negative ")
args = parser.parse_args()

srt = args.srt

with open(srt, 'r+', 'utf-8-sig') as Scroll:
    lini = Scroll.readlines()
Codex = open(basename(srt), 'w+', 'utf-8-sig')

if args.fix[0] == '-':
    positive = False
else:
    positive = True

fix = TimeCode(args.fix)

for pl, line in enumerate(lini):
    try:
        if line[2] == ':':
            line = line.split(' ')
            start = TimeCode(line[0])
            finish = TimeCode(line[2])
            start = start.add(fix, positive)
            finish = finish.add(fix, positive)
            line = [str(start), line[1], str(finish)]
            lini[pl] = ' '.join(line) + '\n'
            print(line)
    except IndexError:
        pass

for line in lini:
    Codex.write(line)
