from Base60 import base60_listise


class TimeCode:

    def __init__(self, call):
        if type(call) is str:
            self.val = timecode_listise(call)
        elif type(call) is list:
            self.val = call

    def add(self, addend, positive=True):
        call = self.val
        addend = addend.val
        back = [(call[0] + addend[0] * (positive * 2 - 1)), []]
        for i in range(3):
            back[1].append(call[1][i] + addend[1][i] * (positive * 2 - 1))
        back[1][0] += back[0] // 1000
        back[0] %= 1000
        for i in range(1, 3):
            back[1][i] += back[1][i - 1] // 60
            back[1][i - 1] %= 60
        return TimeCode(back)

    def expose(self):
        return list_timecodise(self.val)


def timecode_listise(call: str):
    call = call.split(',')[::-1]
    # call is now formated ['ms', 'h:m:s']
    call[1] = base60_listise(call[1])
    # noinspection PyTypeChecker
    call[0] = int(call[0])
    # call is now formated [ms, [s, m, h]]
    return call


def list_timecodise(call: list):
    call[0] = str(call[0])
    call[0] = '0' * (3 - len(call[0])) + call[0]
    for pl, val in enumerate(call[1]):
        val = str(val)
        call[1][pl] = '0' * (2 - len(val)) + val
    call[1] = ':'.join(call[1][::-1])
    back = ','.join(call[::-1])
    return back


if __name__ == "__main__":
    a = TimeCode('00:01:44,479')
    print(a.val)
    b = TimeCode('00:01:44,579')
    c = a.add(b)
    print(c.expose())
