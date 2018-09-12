def getBinaries(s):
    R = []
    for x in s:
        if x > 0.5:
            R.append(1)
        else:
            R.append(0)
    return R

def compute_bin_correlation(b1, b2):
    if len(b1) != len(b2):
        return 0

    n = len(b1)
    k = 0.
    for i in range(n):
        if b1[i] == b2[i]:
            k += 1

    return k/n
