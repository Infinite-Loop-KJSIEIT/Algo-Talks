/**public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc = new Scanner(System.in);
			int n=sc.nextInt();
			int s[]=new int[n];
			
			for(int i =0;i<n;i++)
				s[i]=sc.nextInt();
			
			Arrays.parallelSort(s);
			System.out.println(sub(s));
	}
	
	
	
	public static int sub(int arr[])
	{
		ArrayList<Integer> subset=new ArrayList<Integer>();
		ArrayList<ArrayList<Integer>> set=new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> xorval=new ArrayList<Integer>(); 
			    int suy=0;
			    int index = 0;
			    subsetsUtil(arr, subset, index,set);
			    //System.out.println(set);
			    for(int j=0;j<set.size();j++)
			    {	suy=0;
			    	if(set.size()>=2)
			    	{for(int j1=set.get(j).size()-1;j1>set.get(j).size()-3;j1--)
				    {
			    		suy^=set.get(j).get(j1);				   
			    	
			    	}
			    	xorval.add(suy);}
			    
			    }
			    Collections.sort(xorval);
			    return xorval.get(xorval.size()-1);
	}
	
	
	
	
	public static void subsetsUtil(int[] A,ArrayList<Integer> subset,int index,ArrayList<ArrayList<Integer>> set)
	{
		 
		set.add(new ArrayList<Integer>(subset));
		
		    for(int i=index;i<A.length;i++)  
		    {   
		        
		        subset.add(A[i]);
		          
		       
		        subsetsUtil(A, subset, i + 1,set); 
		          
		        
		        subset.remove(subset.size() - 1);}
		    return;
		    
	}




	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc = new Scanner(System.in);
			int n=sc.nextInt();
			int s[]=new int[n];
			
			Stack<Integer> st = new Stack<>();

			for(int i =0;i<n;i++)
				s[i]=sc.nextInt();
			int ans=0;
			for(int val:s)
			{
				while(!st.isEmpty())
				{
					ans=Math.max(ans,val^st.peek());
					if(st.peek()<n)
					{
						break;
					}
					else
					{
						st.pop();
					}
				}
					
				
				
				st.push(val);
			}
			System.out.println(ans);
			
}
}
	
		public static void main(String args[]){
			Scanner sc=new Scanner(System.in);
			int N=sc.nextInt();
			int n=0,stack[]=new int[100005],ans=0;
			for (int i=1;i<=N;i++)
			{
				int x=sc.nextInt();
				
				
				while (n>0 && x>stack[n]) 
				{
					ans=Math.max(ans,x^stack[n]);
					n--;
				}
				
				if (n>0) 
					ans=Math.max(ans,x^stack[n]);
				
				
				n++;
				stack[n]=x;
			}
			
			System.out.println(ans);
		}
	}
	**/
package DSAPractice;

import java.math.BigInteger;
import java.util.Scanner;
import java.util.Stack;

public class MaxXorSecondary {
/**
public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc = new Scanner(System.in);
			int n=sc.nextInt();
			BigInteger[] s = new BigInteger[n];
			
			

			for(int i =0;i<n;i++)
				s[i]=sc.nextBigInteger();
			BigInteger ans=BigInteger.valueOf(0);
			for(int i =0;i<n;i++)
				for(int j =i+1;j<n;j++)
				{
					ans=ans.max(s[i].xor(s[j]));
				}
					
				
				
			
			System.out.println(ans);
			
}*/
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int n=0,stack[]=new int[100005],ans=0;
		for (int i=1;i<=N;i++)
		{
			int x=sc.nextInt();
			while (n>0 && x>stack[n]) 
			{
				ans=Math.max(ans,x^stack[n]);
				n--;
			}
			
			if (n>0) 
				ans=Math.max(ans,x^stack[n]);
			  
			
			n++;
			stack[n]=x;
		}
		 
		System.out.println(ans);
	}
}
	
	
	
	

