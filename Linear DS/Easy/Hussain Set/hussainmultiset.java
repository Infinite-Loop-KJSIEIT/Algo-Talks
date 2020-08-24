package testJava;
/**
 8 5 3 1
1
2
3
4
6
8

8-------------1
4 5 3 1

5-------------2
4 2 3 1

4-------------3
2 2 3 1

3-------------4
2 2 1 1

2-------------5
1 2 1 1

2-------------6
1 1 1 1

1-------------7 
0 1 1 1

1-------------8
0 0 1 1

1-------------9
0 0 0 1

1-------------10
0 0 0 0



**/
import java.lang.*;
import java.io.*;
import java.util.*;

class hussainmultiset {
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = 0, m = 0;
        
        while (st.hasMoreTokens())
        {
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
        }
        
        
        long[] ar = new long[n];
        
        st = new StringTokenizer(br.readLine());
       
        int e = 0;
        while(st.hasMoreTokens())
        {
            ar[e++] = Long.parseLong(st.nextToken());
        }
        
        
        Arrays.sort(ar);
        
        Queue<Long> q = new ArrayDeque<>();
        
        int i = n - 1;long prev = 0;
        
        while(m-- > 0) 
        {
            long curr = Long.parseLong(br.readLine());
            long val = 0L;
            while (prev < curr) {
                if (i >= 0 && (q.isEmpty() || q.peek() <= ar[i])) {
                    val = ar[i];
                    i--;
                } else {
                    val=q.element();
                    q.remove();
                }

                if (val > 1) {
                    q.add(val / 2);
                }
                prev++;
            }
            System.out.println(val);
        }
        
    }
}
