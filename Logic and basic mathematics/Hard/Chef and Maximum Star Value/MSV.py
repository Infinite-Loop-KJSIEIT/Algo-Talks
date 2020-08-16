for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    validA = [1]*n
    Maxmsv = 0
    for i in range(n-1, -1, -1):
        if(validA[i]):
            if(A[i] == 1):
                print(i)
                break
            msv = 0
            for j in range(0, i):
                if(A[j] % A[i] == 0):
                    validA[j] = 0
                    msv += 1
            Maxmsv = max(Maxmsv, msv)
    print(Maxmsv)
