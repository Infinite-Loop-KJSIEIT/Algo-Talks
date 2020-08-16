def query(i,arr,repeat):
    if i < len(arr):
        return arr[i]
    else:
        return (repeat[(i - len(arr))% len(repeat)])
def solve():
    n = int(input())
    a,b,c = map(int,input().split())
    arr = []
    
    mem = {}
    while True:
        if n in mem:
            break 
        else:
            arr.append(n)
            mem[n] = len(arr)
        n = n/a 
        s = str(n)
        for i in range(len(s)):
            if s[i] == ".":
                if s[i+1] != '0':
                    n = int(s[i+1])
                else:
                    n = int(s[0])
        arr.append(n)
        n = n/b 
        s = str(n)
        for i in range(len(s)):
            if s[i] == ".":
                if s[i+1] != '0':
                    n = int(s[i+1])
                else:
                    n = int(s[0])
        arr.append(n)
        n = n/c 
        s = str(n)
        for i in range(len(s)):
            if s[i] == ".":
                if s[i+1] != '0':
                    n = int(s[i+1])
                else:
                    n = int(s[0])
        
    new_arr = arr[:mem[n]-1]
    repeat = arr[mem[n]-1:]
    #print(new_arr)
    #print(repeat)
    Q = int(input())
    for q in range(Q):
        i = int(input())
        print(query(i, new_arr, repeat))

        



if __name__ == '__main__':
    for t in range(int(input())):
        solve()
