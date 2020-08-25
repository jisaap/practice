알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;

//Given a number represented by a list of digits,
//find the next greater permutation of a number,
//in terms of lexicographic ordering.
//If there is not greater permutation possible,
//return the permutation with the lowest value/ordering.
//
//For example, the list [1,2,3] should 
//return [1,3,2]. The list [1,3,2] should 
//		return [2,1,3]. The list [3,2,1] should 
//				return [1,2,3].
//
//Can you perform the operation without allocating 
//extra memory (disregarding the input memory)?
// update 할것
public class DailyCoding95 {

	
	public static void main(String[] args) {
		int[] arr= {1,3,2};
		ckList(arr);
		System.out.println(Arrays.toString(arr));
	}
	public static void ckList(int[] arr) {
		for(int i = arr.length - 1; i > 0; i --) {
				if(arr[i - 1] <= arr[i]) {
				for(int j = arr.length - 1; j > 0; j --) {
					if(arr[i - 1] >= arr[j]) {
						System.out.println(arr[j]);
						System.out.println(arr[i - 1]);
						int temp = arr[i - 1];
						arr[i - 1] = arr[j];
						arr[j] = temp;
					}
				}
				
			int st = i;
			int en = arr.length - 1;
			while(st < en) {
				int temp = arr[st];
				arr[st] = arr[en];
				arr[en] = temp;
			st ++;
			en --;
			}
			}
		}
		return;
		
	}
	
	
}

```
