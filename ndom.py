def ones(call: int):
    return ['', #0
      "sas",    #1
      "thef",   #2
      "ithin",  #3
      "thonith",#4
      "meregh"  #5
      ][call % 6]

def low_sixes(call: int):
    return ['',     #00
      "mer",        #10
      "mer an thef",#20
      "tondor",     #30
      ][call %4]

def glue(pre : str, post: str):
    glue = bool(pre and post) * " abo "
    return pre + glue + post

def ndom(call: int):
    sases = ones(call)
    low_mers = low_sixes(call // 6)
    back = glue(low_mers, sases)
    return back

for i in range(18+5):
    print(ndom(i))