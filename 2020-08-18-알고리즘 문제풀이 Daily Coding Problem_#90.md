알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Given an integer n and a list of integers l,
//write a function that randomly generates
//a number from 0 to n-1 that isn't in l (uniform).


public class DailyCoding90 {

	public static void main(String[] args) {
		
	Scanner sc = new Scanner(System.in);	
	int n = sc.nextInt();
	List<Integer> l = new ArrayList<Integer>();
	int num = 0;
		while(true) {
			num = sc.nextInt();
			if(num > n - 1)break;
			l.add(num);
		}
		
		System.out.println(calc(n, l));
	}
	
	public static int calc(int n, List<Integer> l) {
		int r = (int)(Math.random() * (n - 1));
		if(l.contains(r)) 	r = calc(n,l);			
		
		return r;
	}
}

```
