def main(inpt: list):
    m = "i"
    r = 0
    q = False
    while not q:
        print("be ", r, "=", inpt[r])
        print(m)
        if m == "i":
            if inpt[r] == 1:
                inpt[r] = "x"
                r += 1
                m = "b"
            elif inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
                m = "p"
        elif m == "p":
            if inpt[r] == 1 or inpt[r] == 2 or inpt[r] == 3 or inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
            elif inpt[r] == "y":
                inpt[r] = "Δ"
                r += 1
                m = "g"
            elif inpt[r] == "Δ":
                q = True
        elif m == "a":
            if inpt[r] == 1:
                r += 1
                m = "b"
            elif inpt[r] == "#":
                inpt[r] = "y"
                r -= 1
                m = "d"
        elif m == "b":
            if inpt[r] == 1:
                inpt[r] = int(2)
                r += 1
                m = "c"
            elif inpt[r] == "#":
                inpt[r] = "y"
                r -= 1
                m = "d"
        elif m == "c":
            if inpt[r] == 1:
                inpt[r] = int(3)
                r += 1
                m = "a"
            elif inpt[r] == "#":
                inpt[r] = "y"
                r -= 1
                m = "d"
        elif m == "d":
            if inpt[r] == 1:
                r -= 1
                m = "e"
            elif inpt[r] == 2:
                r -= 1
                m = "j"
            elif inpt[r] == 3:
                m = "x"
            elif inpt[r] == "x":
                inpt[r] = "Δ"
                r += 1
                m = "p"
        elif m == "e":
            if inpt[r] == 1 or inpt[r] == 2 or inpt[r] == 3:
                r -= 1
            elif inpt[r] == "x":
                inpt[r] = "Δ"
                r += 1
                m = "p"
        elif m == "g":
            if inpt[r] == 1:
                r += 1
            elif inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
                m = "p"
            elif inpt[r] == "Δ":
                q = True
            elif inpt[r] == "y":
                inpt[r] = "Δ"
                r += 1
                m = "k"
        elif m == "j":
            if inpt[r] == 1 or inpt[r] == 2 or inpt[r] == 3:
                r -= 1
            elif inpt[r] == "x":
                inpt[r] = "Δ"
                r += 1
                m = "f"
        elif m == "f":
            if inpt[r] == 1 or inpt[r] == 2 or inpt[r] == 3 or inpt[r] == "y":
                inpt[r] = "Δ"
                r += 1
            elif inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
                m = "g"
        elif m == "x":
            if inpt[r] == 1:
                r -= 1
            elif inpt[r] == 2 or inpt[r] == 3:
                inpt[r] = int(1)
                r -= 1
            elif inpt[r] == "Δ":
                q = True
            elif inpt[r] == "x":
                inpt[r] = int(1)
                r += 1
                m = "g"
        elif m == "k":
            if inpt[r] == 1 or inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
                m = "v"
            elif inpt[r] == "Δ":
                q = True
        elif m == "v":
            if inpt[r] == 1:
                inpt[r] = "Δ"
                r += 1
            elif inpt[r] == "#":
                inpt[r] = "Δ"
                r += 1
                m = "p"
    print("list:")
    print(inpt)


def read_eval():
    inpt = []
    for _ in range(3):
        b = input("Enter three numbers")
        try:
            b = int(b)
        except ValueError:
            if b:
                print('please type a number')
            else:
                return [1, 1, 1, 1, 1, "#", 1, 1, "#", 1, 1, 1, "Δ", "Δ"]
        for __ in range(b):
            inpt.append(1)
        inpt.append("#")
        print(inpt)
    inpt.append("Δ")
    return inpt


if __name__ == "__main__":
    while True:
        main(inpt=read_eval())
