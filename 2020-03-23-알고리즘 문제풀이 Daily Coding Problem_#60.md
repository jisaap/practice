알고리즘 문제풀이



내일 프린트 만들기

```java
package DailyCoding;

import java.util.Arrays;

public class DailyCoding60 {

	
//	Given a multiset of integers, return whether it can be partitioned
//	into two subsets whose sums are the same.
//	For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
//	it would return true, 
//	since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, 
//	which both add up to 55.
//	Given the multiset {15, 5, 20, 10, 35}, it would return false, 
//	since we can't split it up into two subsets that add up to the same sum.
	public static void main(String[] args) {
		
		int[] arr = {15, 5, 20, 10, 35, 15, 10};
//		int[] arr = {15, 5, 20, 10, 35};
		System.out.println(setting(arr));
	}

	
	public static boolean setting(int[] arr) {

		boolean ck = false;
		Arrays.sort(arr);

		if(check(arr[arr.length - 1], arr)) {
			ck = true;
		}else {
			for(int i = 0; i < arr.length - 1; i ++) {
				if(check(arr[arr.length - 1] + arr[i], arr)) {
					ck = true;
					break;
				}else {
					continue;
				}
			}
		}
		return ck;
		
	}
	
	
	public static boolean check(int num, int[] arr) {

		int check = num;
		
		for(int i = 0; i < arr.length; i ++) {
			check -= arr[i];
			if(check == 0) {
				check = num;
			}else if(check < 0) {
				return false;
			}
		}
		
		if(check == num) {
			return true;
		}
		return false;
	}
	
}

```
