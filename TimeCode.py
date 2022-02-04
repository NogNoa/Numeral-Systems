import Base60


class TimeCode:

    def __init__(self, call):
        if type(call) is str:
            self.ms, self.time60 = timecode_variablise(call)
        if type(call) is list:
            self.ms, self.time60 = int(call[0]), call[1]
        self.time60 = [int(i) for i in self.time60]

    def add(self, addend, positive=True):
        back_ms = self.ms + addend.ms * (positive * 2 - 1)
        self.time60[0] += back_ms // 1000
        back_ms %= 1000
        if positive:
            back_time60 = Base60.list_sum_60(self.time60, addend.time60)
        else:
            back_time60 = Base60.subtract_60(self.time60, addend.time60)
        back = [back_ms, back_time60]
        return TimeCode(back)

    def var_timecodise(self):
        ms = f"{self.ms:03d}"
        time60 = self.time60[::]
        for pl, val in enumerate(time60):
            time60[pl] = f"{val:02d}"
        time60 = ':'.join(time60[::-1])
        back = time60 + ',' + ms
        return back

    __str__ = var_timecodise
    expose = var_timecodise
    __add__ = add

    def __sub__(self, subtrend):
        return self.add(subtrend, False)


def timecode_listise(call: str):
    call = call.split(',')[::-1]
    # call is now formatted ['ms', 'h:m:s']
    call[1] = Base60.string_listise(call[1])
    # noinspection PyTypeChecker
    call[0] = int(call[0])
    # call is now formatted [ms, [s, m, h]]
    return call


def timecode_variablise(call: str):
    call = call.split(',')[::-1]
    ms, time60 = int(call[0]), call[1]
    time60 = Base60.string_listise(time60)

    return ms, time60


def list_timecodise(call: list):
    call[0] = f"{call[0]:03d}"
    for pl, val in enumerate(call[1]):
        call[1][pl] = f"{val:02d}"
    call[1] = ':'.join(call[1][::-1])
    back = ','.join(call[::-1])
    return back


if __name__ == "__main__":
    a = TimeCode('0:1:30,009')
    print(a.expose())
    b = TimeCode('00:01:44,579')
    c = a + b
    print(c.expose())
    d = timecode_variablise(a.expose())
    print(d)
    e = b.add(a, positive=False)
    print(e.expose())
    f = TimeCode('-00:11:20,733')
    e = b.add(f)
    print(str(e))
