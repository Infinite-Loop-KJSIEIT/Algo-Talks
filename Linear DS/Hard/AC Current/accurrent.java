package DSAPractice;

import java.util.Scanner;
import java.util.Stack;

public class accurrent {
	
	 
	public static void main(String[] args)
	{
		Scanner sc =new Scanner(System.in);
	    String s=sc.next();
	    Stack<Character> q= new Stack<Character>();
	    for(int i=0;i<s.length();i++)
	    {
	        if(  q.isEmpty()||(s.charAt(i)!=q.peek()) )
	        {
	            q.push(s.charAt(i));
	        }
	        else
	        {
	            q.pop();
	        }
	    }
	    if(q.isEmpty())
	        System.out.println("Yes");
	    else
	    	System.out.println("No");
	}
}
