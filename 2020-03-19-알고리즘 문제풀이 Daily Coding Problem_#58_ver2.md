알고리즘 문제풀이

```java
package daily_Codiong;

import java.util.Arrays;

//n sorted array of integers was rotated an unknown number of times.

//Given such an array, find the index of the element
//in the array in faster than linear time.  ????
//If the element doesn't exist in the array, return null.
//For example, given the array [13, 18, 25, 2, 8, 10] 
//		and the element 8, return 4 (the index of 8 in the array).
//
//You can assume all the integers in the array are unique.

public class DailyCoding58 {

	public static void main(String[] args) {
		int n = 6;
		int[] arr = { 13, 18, 25, 2, 8, 10 };
		int find = 8;
		int st = 0;
		int en = arr.length - 1;

		System.out.println(finder(find, st, en, arr));
		
		Arrays.sort(arr);

		System.out.println(binarySearch(find, st, en, arr));
	}
//      이렇게 하면 더 빠르겠지
	public static int finder(int find, int st, int en, int[] arr) {
		
		for(int i = 0; i < arr.length; i ++) {
			if(arr[i] == find) {
				return i;
			}else if(arr[(arr.length - 1) - i] == find) {
				return (arr.length -1) - i;
			}
		}
			return  -1;
	}
	
	
	
	
	public static int binarySearch(int find, int st, int en, int[] arr) {

		int i = (st + en) / 2;

		if (arr[i] == find) {
			return i;
		} else if (arr[i] > find) {
			en = i - 1;
		} else if(arr[i] < find){
			st = i + 1;
		}else {
			return -1;
		}
		return binarySearch(find, st, en, arr);

	}

}

```
