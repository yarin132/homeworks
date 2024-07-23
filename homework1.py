def bin_convert(mem, number):
    x = bin(number)[2:]
    x = x.zfill(mem)
    rev_x = []
    for b in x:
        if int(b):
            rev_x.append("0")
        else:
            rev_x.append("1")
    for i in range(len(rev_x))[::-1]:
        if int(rev_x[i]):
            rev_x[i] = "0"
        else:
            rev_x[i] = "1"
            break
    print("".join(rev_x))


def main():
    mem = int(input("pls enter the mem(bytes) size: ")) * 8
    number = int(input("pls enter the number: "))
    bin_convert(mem, number)


if __name__ == "__main__":
    main()
