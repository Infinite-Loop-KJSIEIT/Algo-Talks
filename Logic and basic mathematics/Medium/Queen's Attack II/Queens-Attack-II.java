import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args)
    {
       
        int n = sc.nextInt();
        int k = sc.nextInt();
        int r_q = sc.nextInt();
        int c_q = sc.nextInt();
        int[][] ob = new int[k][2];
        int u=n+1,d=n+1,l=n+1,r=n+1,ur=n+1,ul=n+1,dr=n+1,dl=n+1;
        for (int i = 0; i < k; i++) 
        {
         ob[i][0]= sc.nextInt();
         ob[i][1]= sc.nextInt();
         if(ob[i][0]==r_q)
         {
            if(c_q>ob[i][1] && c_q-ob[i][1]-1<l)
                l=c_q-ob[i][1]-1;
            if(c_q<ob[i][1] && -c_q+ob[i][1]-1<r)
                r=-c_q+ob[i][1]-1;
         }
         if(ob[i][1]==c_q)
         {
            if(r_q>ob[i][0] && r_q-ob[i][0]-1<d)
                d=r_q-ob[i][0]-1;
            if(r_q<ob[i][0] && -r_q+ob[i][0]-1<u)
                u=-r_q+ob[i][0]-1;
         }
         if(ob[i][0]-r_q==ob[i][1]-c_q)
         {
            if(ob[i][0]-r_q>0 && ob[i][0]-r_q-1<ur)
                ur=ob[i][0]-r_q-1;
            if(ob[i][0]-r_q<0 && -ob[i][0]+r_q-1<dl)
                dl=-ob[i][0]+r_q-1;
         }
         if(ob[i][0]-r_q==(ob[i][1]-c_q)*(-1))
         {
            if(ob[i][0]-r_q>0 && ob[i][0]-r_q-1<ul)
                ul=ob[i][0]-r_q-1;
            if(ob[i][0]-r_q<0 && -ob[i][0]+r_q-1<dr)
                dr=-ob[i][0]+r_q-1;
         }
        }
        if(u==n+1)
        u=n-r_q;
        if(d==n+1)
        d=r_q-1;
        if(r==n+1)
        r=n-c_q;
        if(l==n+1)
        l=c_q-1;

        if(ur==n+1)
        ur=Math.min(n-r_q, n-c_q);
        if(ul==n+1)
        ul=Math.min(n-r_q, c_q-1);
        if(dr==n+1)
        dr=Math.min(r_q-1, n-c_q);
        if(dl==n+1)
        dl=Math.min(r_q-1, c_q-1);

        System.out.println(u+d+r+l+ur+ul+dr+dl);

       


    }
}