from sys import stdin


def read_positions(it, m, cnt):
    """Expand interval inputs into sorted position lists."""
    arr = []
    for _ in range(cnt):
        L = next(it)
        R = next(it)
        step = (R - L) // m
        for k in range(step + 1):
            arr.append(L + k * m)
    arr.sort()
    return arr


def group_cost(c, L, R):
    """Cost for cow at position c to pick packages from L to R."""
    if L > R:
        return 0
    return (R - L) + min(abs(c - L), abs(c - R))


def compute_dp(cows, pkgs):
    """Dynamic program using divide and conquer optimization."""
    C, P = len(cows), len(pkgs)
    INF = 10 ** 18

    prev = [0] + [INF] * P
    curr = [INF] * (P + 1)

    def solve(i, l, r, opt_l, opt_r):
        if l > r:
            return
        mid = (l + r) // 2
        best_val = INF
        best_k = opt_l
        start = max(0, opt_l)
        end = min(mid - 1, opt_r)
        for k in range(start, end + 1):
            if prev[k] == INF:
                continue
            val = prev[k] + group_cost(cows[i], pkgs[k], pkgs[mid - 1])
            if val < best_val:
                best_val = val
                best_k = k
        curr[mid] = best_val
        solve(i, l, mid - 1, opt_l, best_k)
        solve(i, mid + 1, r, best_k, opt_r)

    for i in range(C):
        curr[0] = 0
        solve(i, 1, P, 0, P - 1)
        prev, curr = curr, [INF] * (P + 1)
    return prev[P]


def main():
    data = list(map(int, stdin.read().split()))
    if not data:
        return
    it = iter(data)
    M, N, P = next(it), next(it), next(it)
    cows = read_positions(it, M, N)
    pkgs = read_positions(it, M, P)
    ans = compute_dp(cows, pkgs)
    print(ans)


if __name__ == "__main__":
    main()
