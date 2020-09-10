알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Date;

//Given a function f, and N return a debounced f of N milliseconds.

//That is, as long as the debounced f continues to be invoked,
//f itself will not be called for N milliseconds.

public class DailyCoding105 {

	public static void main(String[] args) {
		final int N = 1000;
		System.out.println(f(N));
	}
	
	public static long f(int n) {
		try {
			Thread.sleep(n);
		}catch(Exception e) {
			e.printStackTrace();
		}
		return System.currentTimeMillis();
	}
	
}

```
