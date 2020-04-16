알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//A number is considered perfect if its digits sum up to exactly 10.
//
//Given a positive integer n, return the n-th perfect number.
//
//For example, given 1, you should return 19. Given 2, you should return 28.


public class DailyCoding70 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int num = 10 - n;
		
		System.out.println(n+""+num);
		
	}
}

```
