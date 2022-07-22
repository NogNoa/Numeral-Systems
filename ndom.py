def ones(call: int):
    return ['', #0
      "sas",    #1
      "thef",   #2
      "ithin",  #3
      "thonith",#4
      "meregh"  #5
      ][call % 6]

def sixes(call: int):
    return ['',     #00
      "mer",        #10
      "mer an thef",#20
      ][call %3]

def glue(pre : str, post: str):
    glue = bool(pre and post) * " abo "
    return pre + glue + post

def ndom(call: int):
    sases = ones(call)
    mers = sixes(call // 6)
    tondor = (call // 18 % 2) * "tondor"
    nif = (call // 36 % 2) * "nif"
    back = glue(mers, sases)
    back = glue(tondor, back)
    back = glue(nif, back)
    return back

for i in range(36*2):
    print(ndom(i))