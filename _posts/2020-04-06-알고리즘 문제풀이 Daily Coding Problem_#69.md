알고리즘 문제풀이



```java
package DailyCoding;

//Given a list of integers, 
//return the largest product that can be 
//		made by multiplying any three integers.
//
//For example,
//if the list is [-10, -10, 5, 2],
//we should return 500, since that's -10 * -10 * 5.
//
//You can assume the list has at least three integers.

public class DailyCoding69 {

	
	public static void main(String[] args) {

		int[] arr = {-10, -10, 5, 2};
		int result = 0;
		int temp = 0;
		int x = 0;
		int y = 0;
		
		for(int i = 1; i < arr.length; i ++ ) {
			for(int j = 0; j < i; j ++) {
				if(temp < arr[i] * arr[j]) {
					temp = arr[i] * arr[j];
					x = i;
					y = j;
				}
			}
		}
		
		for(int i = 0; i < arr.length; i ++) {
			if(i == x || i == y) {
				continue;
			}
			result = Math.max(result, temp * arr[i]);
		}
		System.out.println(result);
	}
	
}

```
