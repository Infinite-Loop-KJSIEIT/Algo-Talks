    """
    Problem link:https://www.codechef.com/problems/COOK82C
    Solution By Keshav Mishra 
    """
    from sys import stdin,stdout
    def input(): return stdin.readline().strip()
    from collections import deque

    # def print(s): stdout.write(str(s)+'\n')


    def solve():
        n, m = map(int, input().split())
        freq = dict()
        elements = list(map(int, input().split()))
        elements.sort(reverse = True)
        elements = deque(elements)
        queue = deque()

        queries = []
        for i in range(m):
            queries.append(int(input()))
        max_queries = queries[-1]
        
        query_ans = []
        i = 1
        idx = 0
        while i <= max_queries:
            if len(queue):
                if len(elements)== 0 or queue[0] > elements[0]:
                    element = queue.popleft()
                else:
                    element = elements.popleft()
            else:
                element = elements.popleft()
            query_ans.append(element)
            element //= 2 
            if element:
                queue.append(element)
            i += 1 
            if len(query_ans) >= queries[idx]:
                print(query_ans[queries[idx]-1])
                idx += 1
        
            
        


    if __name__ == '__main__':
        solve()
        