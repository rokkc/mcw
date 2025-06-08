import random, os, sys
from math import inf

random.seed(0)
NUM_CASES = 20

def compute(M, cow_intervals, pkg_intervals):
    cows = []
    for L, R in cow_intervals:
        for x in range((R - L) // M + 1):
            cows.append(L + x * M)
    pkgs = []
    for A, B in pkg_intervals:
        for x in range((B - A) // M + 1):
            pkgs.append(A + x * M)
    cows.sort()
    pkgs.sort()
    C, P = len(cows), len(pkgs)
    INF = 10 ** 18
    dp = [[INF] * (P + 1) for _ in range(C + 1)]
    for i in range(C + 1):
        dp[i][0] = 0
    for i in range(1, C + 1):
        for j in range(1, P + 1):
            best = INF
            for k in range(j):
                if dp[i - 1][k] == INF:
                    continue
                L = pkgs[k]
                R = pkgs[j - 1]
                cost = (R - L) + min(abs(cows[i - 1] - L), abs(cows[i - 1] - R))
                candidate = dp[i - 1][k] + cost
                if candidate < best:
                    best = candidate
            dp[i][j] = best
    return dp[C][P]

cases = []
for _ in range(NUM_CASES):
    M = random.randint(1, 10)
    N = random.randint(1, 3)
    P = random.randint(1, 3)
    c_int = []
    for _ in range(N):
        L = random.randint(0, 20)
        mult = random.randint(0, 3)
        R = L + mult * M
        c_int.append((L, R))
    p_int = []
    for _ in range(P):
        A = random.randint(0, 20)
        mult = random.randint(0, 3)
        B = A + mult * M
        p_int.append((A, B))
    ans = compute(M, c_int, p_int)
    cases.append((M, N, P, c_int, p_int, ans))

os.makedirs('testcases', exist_ok=True)
for idx, (M, N, P, c_int, p_int, ans) in enumerate(cases, 1):
    with open(f'testcases/case{idx}.in', 'w') as f:
        f.write(f"{M} {N} {P}\n")
        for L, R in c_int:
            f.write(f"{L} {R}\n")
        for A, B in p_int:
            f.write(f"{A} {B}\n")
    with open(f'testcases/case{idx}.out', 'w') as f:
        f.write(str(ans) + "\n")
    print(f"Case {idx}: output {ans}", file=sys.stderr)
