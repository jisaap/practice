알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

public class DailyCoding85 {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		int y = sc.nextInt();
		int b = (int)(Math.random() *2);
		
		System.out.println((b|b )* x + (~b + 2) * y);
	}
}

```

