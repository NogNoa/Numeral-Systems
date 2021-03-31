from codecs import open
from TimeCode import TimeCode

folder = 'The Morning Show Season 1 Mp4 1080p/'
name = 'The.Morning.Show.S01E02.WEB.x264-PHOENiX-eng.srt'

with open("D:/Videos/Telly/"+folder+name, 'r+', 'utf-8-sig') as Scroll:
    lini = Scroll.readlines()
Codex = open(name, 'w+', 'utf-8-sig')

fix = '0:0:01,343'
positive = 1

fix = TimeCode(fix)

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
