알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Scanner;

//You have n fair coins and you flip them all at the same time.
// Any that come up tails you set aside. The ones that come up heads you flip again.
//How many rounds do you expect to play before only one coin remains?

//Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

public class DailyCoding124 {

	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println(flip(sc.nextInt()));
	}
	
	public static int flip(int n) {
		int[] arr = new int[n];
		int count = 0;
		while(count != 1) {
			count = 0;
		for(int i = 0; i < n; i ++) {
			if(arr[i] == 1)continue;
			arr[i] = (int)(Math.random() * 2) + 1;
			count ++;
		}
		if(count == 0)arr = new int[n];
	}
		return count;

		
	}
}

```
