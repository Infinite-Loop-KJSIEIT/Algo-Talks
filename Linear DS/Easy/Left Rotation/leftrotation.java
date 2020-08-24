import java.io.*;
import java.util.*;

public class leftrotation {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int d = in.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            if(d > i) 
                arr[n - d + i] = in.nextInt();
            else
                arr[i - d] = in.nextInt();
        }
        
        for(int i = 0; i < n; i++)
            System.out.print(arr[i] + " ");
    }
}
