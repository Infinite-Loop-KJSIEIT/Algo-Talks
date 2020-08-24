package testJava;
import java.util.*;
public class boatscompetition
{
	public static void main(String[] args)
	{
	  Scanner s=new Scanner(System.in);
	  int t=s.nextInt();
	  
	   while(t>0)
	   {
		int n=s.nextInt();
		int a[] = new int[n];
		for(int i=0;i<n;i++)
		{
		a[i]=s.nextInt();
		}
		int Ans=0;
		for(int i=100;i>1;i--)
		{
		  int ans=0;
		  boolean bl[]=new boolean[n];
		  for(int j=0;j<n-1;j++)
		   {
		    
			  for(int k=j+1;k<n;k++)
			  {
				  
				  if( a[j]+a[k] == i && (!bl[k]) && (!bl[j]) )
				  {
					  ans++;
					  bl[k]=true;
					  break;
				  }
				  
			  }
			  
		   }
 
 
		 Ans=Math.max(Ans,ans);
		}
		System.out.println(Ans);
	   t--;
	   }
            	  
	}
}
