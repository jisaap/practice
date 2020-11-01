알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Write a function that rotates a list by k elements. 
//	For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
//	Try solving this without creating a copy of the list.
//	How many swap or move operations
//	do you need?

public class DailyCoding126 {

	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner (System.in);
		List<Integer> result = new ArrayList<Integer>();
		int k = sc .nextInt();
		
		for(int i = 0; i < k; i ++) {
		result = swap(result, k);
		}
		System.out.println(result);
	}
	
	public static List<Integer> swap(List<Integer> list, int k) {
			list.add(list.get(0));
			list.remove(0);
		return list;
	}
	
}

```
