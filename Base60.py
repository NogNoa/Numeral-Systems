from collections import deque


def base60_decimise(call: str):
    call = string_listise(call)
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


def string_listise(call: str):
    call = call.split(':')[::-1]  # '20:15' becomes ['15','20']
    call = [int(val) for val in call]
    return call


def list_stringise(call: list):
    call = [str(val) for val in call]
    call = ':'.join(call[::-1])
    return call


def carry_60(call: list):
    back = []
    call.append(0)
    # gives us as much additional hexacontamal digits as needed.
    # if most significant digit is 0 log will fail and the subroutine is unneeded.
    #
    carry = 0
    for pl, val in enumerate(call):
        bck_val = val + carry
        if bck_val > 59:
            carry = bck_val // 60
            bck_val %= 60
        else:
            carry = 0
        back.append(bck_val)
    if back[-1] == 0:
        del(back[-1])
    return back


def list_sum_60(*call):
    """

    :param positive: True:addition  False:subtraction
    :param call: a tuple of base60 lists
    :return: a base 60 list which is the sum of all of them
    """
    mxlen = max(len(lst) for lst in call)
    back = [0] * mxlen
    for lst in call:
        for pl, val in enumerate(lst):
            back[pl] += val
    back = carry_60(back)
    return back


def string_sum_60(*cali):
    """

    :param cali: strings of base60 numbers
    :return: string of base60 numbers
    """
    cali = tuple(string_listise(call) for call in cali)
    # cali = map(base60_listise, cali)
    back = list_sum_60(*cali)
    back = list_stringise(back)
    return back


def subtract_60(minuend, subtrahend):
    back = []
    Δ = len(subtrahend) - len(minuend)
    minuend += [0] * Δ
    for i, val in enumerate(minuend):
        back.append(val - subtrahend[i])
    back = carry_60(back)
    return back


base60_sum = string_sum_60

"""

def base60_list_sum2(*call, sam=None):
    """
"""
    completely unusable :-)
    :param call: a tuple of base60 lists
    :param sam: partial sum in the computation
    :return: a base 60 list which is the sum of all of them
    """
"""
    call = deque(call)
    if sam is None:
        sam = []
    lst = call[0]
    Δ = len(lst) - len(sam)
    sam += [0] * Δ
    for pl, val in enumerate(lst):
        sam[pl] += val
    if call[0] is call[-1]:
        return sam
    else:
        call.popleft()
        newsum = base60_list_sum2(call, sam)
        return newsum
"""
