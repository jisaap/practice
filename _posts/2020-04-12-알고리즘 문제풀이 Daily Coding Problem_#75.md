알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;

//Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.
//
//For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.


public class DailyCoding75 {

	static int arr[] = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
	
	static int[] result = new int[arr.length];
	
	public static void main(String[] args) {
		

		for(int i = 0; i < arr.length; i++) {
			result[i] = 1;
			for(int j = 0; j < i; j ++) {
				if(arr[i] > arr[j]) {

					result[i] = Math.max(result[i], result[j] + 1);
				}
			}
		}
		
		int count = result[arr.length - 1];
		int[] val = new int[count];
		System.out.println(count);
		System.out.println(Arrays.toString(makeArray(arr.length - 1, count, val)));
		
	}
	
	public static int[] makeArray(int x,  int c, int[] v) {
		
		if(c == 0) {
			return v;
		}
		
		for(int i =  x; i >= 0; i --) {
			if(c == result[i]) {
				v[c -1] = arr[i];
				makeArray(i, c - 1, v);
				break;
			}
		}
		return v;
	}

}

```
