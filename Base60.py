from collections import deque
from math import log


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


def base60_carry(call: list):
    back = []
    power = int(log(call[-1], 60))
    call.extend([0]*power)
    # gives us as much additional hexacontamal digits as needed
    carry = 0
    for pl, val in enumerate(call):
        bval = val + carry
        if bval > 59:
            carry = bval // 60
            bval %= 60
        else:
            carry = 0
        back.append(bval)
    return back


def base60_list_sum(*call):
    """

    :param call: a tuple of base60 lists
    :return: a base 60 list which is the sum of all of them
    """
    mxlen = max(len(lst) for lst in call)
    back = [0] * mxlen
    for lst in call:
        for pl, val in enumerate(lst):
            back[pl] += val
    back = base60_carry(back)
    return back


def base60_string_sum(*cali):
    """

    :param cali: strings of base60 numbers
    :return: string of base60 numbers
    """
    cali = tuple(base60_listise(call) for call in cali)
    # cali = map(base60_listise, cali)
    back = base60_list_sum(*cali)
    back = base60_delistise(back)
    return back


base60_sum = base60_string_sum


def base60_list_sum2(*call, sum=[]):
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
        newsum = base60_list_sum2(*call,sum)
        return newsum

# Todo: make base60_sum2 recusive that's just kinda intresting :-)
