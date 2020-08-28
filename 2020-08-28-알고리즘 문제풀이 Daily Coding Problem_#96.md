알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;

//Given a number in the form of a list of digits, 
//return all possible permutations.

//For example,
//given [1,2,3],
//return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].

public class DailyCoding96 {

	static int[] arr = {1,2,3};
	public static void main(String[] args) {
		System.out.println(Arrays.toString(arr));
		boolean ck = true;
		while(ck) {
			for(int i = arr.length - 1; i > 0; i --) {
				if(arr[i - 1] < arr[i]) {
					splitArr(i);
					ck = true;
					System.out.println(Arrays.toString(arr));
					break;
				}else {
					ck = false;
				}
			}
		}
		
		
	}
	
	public static void splitArr(int n) {
		for(int i = arr.length - 1; i >= n; i --) {
			for(int j = n - 1; j >= 0; j --) {
				if(arr[i] > arr[j]) {
					swap(i, j);
					sortRight(n);
					return;
				}
			}
		}
	}
	
	public static void swap(int a, int b) {
		int temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
		
	}
	
	public static void sortRight(int n) {
		for(int i = n; i < arr.length - 1; i ++) {
			for(int j = i + 1; j <= arr.length - 1; j ++) {
				if(arr[i] > arr[j])swap(i, j);
			}
		}
	}
}

```
