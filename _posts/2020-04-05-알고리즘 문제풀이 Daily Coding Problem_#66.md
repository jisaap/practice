알고리즘 문제풀이



```java
package DailyCoding;


//Assume you have access to a function toss_biased()
//which returns 0 or 1 with a probability 
//that's not 50-50 (but also not 0-100 or 100-0). 
//You do not know the bias of the coin.
//
//Write a function to simulate an unbiased coin toss.


public class DailyCoding66 {

	
	public static void main(String[] args) {
		
		System.out.println(toss_biased());
		
	}
	
	public static int toss_biased() {
		
		int n = 0;
		
		n = (int)(Math.random() * 2);
		
		return n;
	}
}

```
