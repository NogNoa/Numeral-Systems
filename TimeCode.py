import Base60


class TimeCode:

    def __init__(self, call):
        if type(call) is str:
            self.val = timecode_listise(call)
        elif type(call) is list:
            self.val = call

    def add(self, addend, positive=True):
        call = self.val
        addend = addend.val
        miliseconds = (call[0] + addend[0] * (positive * 2 - 1))
        call[1][0] += miliseconds // 1000
        miliseconds %= 1000
        if positive:
            time60 = Base60.base60_list_sum(call[1], addend[1])
        else:
            time60 = [0]
            for i in range(3):
                time60.append(call[1][i] - addend[1][i])
                try:
                    time60[i] += time60[1][i - 1] // 60
                    time60[1][i - 1] %= 60
                except IndexError:
                    pass
        back = [miliseconds, time60]
        return TimeCode(back)

    def expose(self):
        return list_timecodise(self.val)


def timecode_listise(call: str):
    call = call.split(',')[::-1]
    # call is now formated ['ms', 'h:m:s']
    call[1] = Base60.base60_listise(call[1])
    # noinspection PyTypeChecker
    call[0] = int(call[0])
    # call is now formated [ms, [s, m, h]]
    return call


def list_timecodise(call: list):
    call[0] = f"{call[0]:03d}"
    for pl, val in enumerate(call[1]):
        call[1][pl] = f"{val:02d}"
    call[1] = ':'.join(call[1][::-1])
    back = ','.join(call[::-1])
    return back


if __name__ == "__main__":
    a = TimeCode('0:1:44,009')
    print(a.val)
    b = TimeCode('00:01:44,579')
    c = a.add(b)
    print(c.expose())
    d = list_timecodise(a.val)
    print(d)
