알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

//Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
//
//The input list is not necessarily ordered in any way.
//
//For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


public class DailyCoding77 {

	public static void main(String[] args) {
		
		int[][] arr = 1, 3, 5, 8, 4, 10, 20, 25;
		
//		System.out.print(Arrays.toString(arr[0]));
		int[][] result = check(arr);
		for(int i = 0; i < result.length; i ++) {
			System.out.print(Arrays.toString(result[i]));
		}
	
	}
	
	public static int[][] check(int[][] arr) {
		ArrayList<int[]> list = new ArrayList<int[]>();
			for(int i = 0; i < arr.length; i ++) {
				for(int j = 0; j < arr.length; j ++) {
					
				if(arr[i][0] > arr[j][0] && arr[i][1] < arr[j][1]) {
					break;
				}else if(j == arr.length - 1) {
					list.add(new int[] {arr[i][0], arr[i][1]});
				}
				}
			}
			int[][] result = new int[list.size()][2];
			
			for(int i = 0; i < list.size(); i ++) {
				result[i][0] = list.get(i)[0];
				result[i][1] = list.get(i)[1];
			}
			return result;
	}
	
}

```

