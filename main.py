from sys import stdin

def main():
    data=list(map(int, stdin.read().strip().split()))
    if not data:
        return
    it=iter(data)
    M=next(it); N=next(it); P=next(it)
    cows=[]
    for _ in range(N):
        L=next(it); R=next(it)
        for k in range((R-L)//M+1):
            cows.append(L+k*M)
    pkgs=[]
    for _ in range(P):
        A=next(it); B=next(it)
        for k in range((B-A)//M+1):
            pkgs.append(A+k*M)
    cows.sort()
    pkgs.sort()
    C=len(cows); P=len(pkgs)
    INF=10**18
    dp=[[INF]*(P+1) for _ in range(C+1)]
    for i in range(C+1):
        dp[i][0]=0
    for i in range(1,C+1):
        for j in range(1,P+1):
            best=INF
            for k in range(j):
                if dp[i-1][k]==INF:
                    continue
                L=pkgs[k]
                R=pkgs[j-1]
                cost=(R-L)+min(abs(cows[i-1]-L), abs(cows[i-1]-R))
                cand=dp[i-1][k]+cost
                if cand<best:
                    best=cand
            dp[i][j]=best
    print(dp[C][P])

if __name__=='__main__':
    main()
