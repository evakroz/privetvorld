def calc_pi(param):
    cnt = 0
    pi = 0
    while cnt < param:
        if cnt % 2 == 0:
            pi = pi - 4/(cnt+1)
        else:
            pi = pi + 4/(cnt+1)

        cnt = cnt +1

    return cnt


if __name__ == '__main__':
    pi = calc_pi(10)
    print(pi)