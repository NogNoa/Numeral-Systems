from collections import deque

def base60_decimise(call: str):
    call = base60_listise(call)
    depth = len(call)
    back = 0
    for pl, val in enumerate(call):
        back += val * 60 ** pl
    return back, depth


def base10_haxacontamise(call: int, depth=3):
    """that is turn base 10 to base 60"""
    back = ''
    for i in range(depth):
        back = str(call % 60) + ':' + back
        call = call // 60
    back = back[:-1]
    return back


def base60_listise(call: str):
    call = call.split(':')[::-1]  # '20:15' becomes ['15','20']
    call = [int(val) for val in call]
    return call


def base60_sum(*call):
    """

    :param call: a tuple of base60 lists
    :return: a base 60 list which is the sum of all of them
    """
    mxlen = max(len(lst) for lst in call)
    back = [0] * mxlen
    for lst in call:
        for pl, val in enumerate(lst):
            back[pl] += val
    return back


def base60_sum2(*call):
    """

    :param call: a tuple of base60 lists
    :return: a base 60 list which is the sum of all of them
    """
    mxlen = max(len(lst) for lst in call)
    q = deque(call)
    back = [0] * mxlen
    while q:
        for pl, _ in enumerate(back):
            back[pl] += q[0][pl]
        q.popleft()
        rest = base60_sum2(q)
    return back


