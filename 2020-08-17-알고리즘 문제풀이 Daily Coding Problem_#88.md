알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//Implement division of two positive integers without using
//the division, multiplication, or modulus operators.
//Return the quotient as an integer, ignoring the remainder.

public class DailyCoding88 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int sum = 0;
		int count = 0;
		
		while(a > sum) {
			sum += b;
			count ++;
		}
		
		if(a != sum) count--;
		
		System.out.println(count);
	}
}

```
