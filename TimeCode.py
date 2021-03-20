import Base60


class TimeCode:

    def __init__(self, call):
        if type(call) is str:
            self.ms, self.time60 = timecode_variablise(call)
        if type(call) is list:
            self.ms, self.time60 = int(call[0]), call[1]
        self.time60 = [int(i) for i in self.time60]

    def __str__(self):
        return self.expose()

    def add(self, addend, positive=True):
        back_ms = (self.ms + addend.ms * (positive * 2 - 1))
        self.time60[0] += back_ms // 1000
        back_ms %= 1000
        if positive:
            back_time60 = Base60.base60_list_sum(self.time60, addend.time60)
        else:
            back_time60 = [0]
            for i in range(3):
                back_time60.append(self.time60[i] - addend.time60[i])
                try:
                    back_time60[i] += back_time60[1][i - 1] // 60
                    back_time60[1][i - 1] %= 60
                except IndexError:
                    pass
        back = [back_ms, back_time60]
        return TimeCode(back)

    def expose(self):
        return self.var_timecodise()

    def var_timecodise(self):
        ms = f"{self.ms:03d}"
        time60 = self.time60
        for pl, val in enumerate(time60):
            time60[pl] = f"{val:02d}"
        time60 = ':'.join(time60[::-1])
        back = time60 + ',' + ms
        return back


def timecode_variablise(call: str):
    call = call.split(',')[::-1]
    ms, time60 = int(call[0]), call[1]
    time60 = Base60.base60_listise(time60)

    return ms, time60


def list_timecodise(call: list):
    call[0] = f"{call[0]:03d}"
    for pl, val in enumerate(call[1]):
        call[1][pl] = f"{val:02d}"
    call[1] = ':'.join(call[1][::-1])
    back = ','.join(call[::-1])
    return back


if __name__ == "__main__":
    a = TimeCode('0:1:44,009')
    print(a.expose())
    b = TimeCode('00:01:44,579')
    c = a.add(b)
    print(c.expose())
    d = timecode_variablise(a.expose())
    print(d)

# todo: wtf why time60 items turn to strings
#  get substracting back to add