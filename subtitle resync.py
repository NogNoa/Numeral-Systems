from codecs import open
from TimeCode import TimeCode

folder ='Normal.People.S01/'
name ='Normal.People.S01E02.he.srt'

Scroll = open("D:/Videos/Telly/"+folder+name, 'r+', 'utf-8')
Codex = open(name, 'w+', 'utf-8')

fix = '0:0:0,17'
positive = 0

fix = TimeCode(fix)

lini = Scroll.readlines()


for pl, line in enumerate(lini):
    try:
        if line[2] == ':':
            line = line.split(' ')
            start = TimeCode(line[0])
            finish = TimeCode(line[2])
            start = start.add(fix, positive)
            finish = finish.add(fix, positive)
            line = [start.expose(), line[1], finish.expose()]
            lini[pl] = ' '.join(line) + '\n'
    except IndexError:
        pass

for line in lini:
    Codex.write(line)
