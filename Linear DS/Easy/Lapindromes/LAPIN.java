/** 
 * this one worked:
 * 
 * for _ in range(int(input())):
    s=input()
    l=len(s)//2
    mid=int(l+(0 if len(s)%2==0 else 1))
    fh=s[0:l]
    sh=s[mid:len(s)]
    x=sorted(fh)
    y=sorted(sh)
    X=''.join(x)
    Y=''.join(y)
    if X==Y:
        print("yes")
    else:
        print("no")

 */

package DSAPractice;
import java.util.*;
class LAPIN
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    String s=sc.next();
		    
		    int mid=(s.length()/2+(s.length()%2==0?0:1));
		    char fh[]=new char[s.length()/2];
		    char sh[]=new char[s.length()/2];
		    for(int i =0;i<s.length()/2;i++)
		    {
		        fh[i]=s.charAt(i);
		        
		    }
		    for(int j =0;j<s.length()/2;j++)
		    {
		        sh[j]=s.charAt(j+mid);
		        
		    }
		    
		    
		    Arrays.sort(sh);
		    Arrays.sort(fh);
		    String SH=String.valueOf(sh);
		    String FH=String.valueOf(sh);
		    
		    if(SH.equals(FH)==true)
		    {
		        System.out.println("YES");
		        
		    }
		    else{
		         System.out.println("NO");
		    }
		}
	}
}
