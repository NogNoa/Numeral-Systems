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
    for _ in range(depth):
        back = str(call % 60) + ':' + back
        call = call // 60
    back = back[:-1]
    return back


def base60_listise(call: str):
    call = call.split(':')[::-1]  # '20:15' becomes ['15','20']
    call = [int(val) for val in call]
    return call


def base60_delistise(call: list):
    call = [str(val) for val in call]
    call = ':'.join(call[::-1])
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


def base60_complete_sum(*cali):
    cali = tuple(base60_listise(call) for call in cali)
    back = base60_sum(cali)
    back = base60_delistise(back)
    return back


def base60_sum2(*call,sum =[]):
    """

    :param call: a tuple of base60 lists
    :return: a base 60 list which is the sum of all of them
    """
    lst = call[0]
    Δ =  len(lst) - len(sum)
    sum += [0] * Δ
    for pl, val in enumerate(lst):
        sum[pl] += val
    if call[0] is call[-1]:
        return sum
    else:
        call = call[1:]
        newsum = base60_sum2(*call,sum)
        return newsum

# Todo: make base60_sum2 recusive that's just kinda intresting :-)
