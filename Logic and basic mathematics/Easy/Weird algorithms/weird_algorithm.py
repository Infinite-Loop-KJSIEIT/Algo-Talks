"""
Problem Link : https://cses.fi/problemset/task/1068/
"""
def solve():
    n = int(input())
    print(n, end = " ")
    while n!=1:
        if n%2:
            n = 3*n + 1 
            print(n, end = " ")
        else:
            n //= 2 
            print(n, end = " ")
 
 
if __name__ == '__main__':
    solve()
