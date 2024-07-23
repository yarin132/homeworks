import sys
import os


def count_sort(file, N):
    with open(file) as rfile:
        sp_text = rfile.read().split()
        n_dict = {}
        for t in sp_text:
            if t in n_dict.keys():
                n_dict[t] += 1
            else:
                n_dict[t] = 1
    s_dict = dict(sorted(n_dict.items(), key=lambda x: x[1], reverse=True))
    i = 0
    for item in s_dict.items():
        print(item)
        i += 1
        if i == N:
            break


def main():
    if len(sys.argv) == 3:
        if not os.path.exists(sys.argv[1]):
            print("something is wrong with the file.")
        elif not sys.argv[2].isnumeric():
            print("N is not a numeric.")
        elif not int(sys.argv[2]) > 0:
            print("N needs to be larger than 0.")
        else:
            count_sort(sys.argv[1], int(sys.argv[2]))
    else:
        print("not enough or no arguments given.")


if __name__ == "__main__":
    main()