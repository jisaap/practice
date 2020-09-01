알고리즘 문제풀이



```java
package DailyCoding;

import java.util.HashSet;

//Given an unsorted array of integers, 
//find the length of the longest consecutive elements sequence.
//
//For example, given [100, 4, 200, 1, 3, 2], 
//the longest consecutive element sequence is [1, 2, 3, 4].
//Return its length: 4.
//
//Your algorithm should run in O(n) complexity.

public class DailyCoding99 {

	
	public static void main(String[] args) {
		
		int[] arr = {100, 4, 200, 1, 3, 2};
		HashSet<Integer> set = new HashSet<Integer>();
		int result = 0;
		
		for(int a : arr)set.add(a);
		
		for(int a : arr) {
			int count = 1;
			
			int under = a - 1;
			while(set.contains(under)) {
				set.remove(under);
				under --;
				count ++;
			}
			
			int over = a + 1;
			while(set.contains(over)) {
				set.remove(over);
				over ++;
				count ++;
			}
			result = Math.max(result, count);
		}
		System.out.println(result);
	}
	
}

```
