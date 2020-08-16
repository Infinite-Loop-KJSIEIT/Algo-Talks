if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
 
        a.sort(reverse=True)
        # print(a)
        for i in range(n):
            if a[i] <= n - i:
                print(n - i + 1)
                break
 
        else:
            print(1)
