알고리즘 문제풀이



```java
package DailyCoding;

import java.util.ArrayList;
import java.util.List;

//Given a list of integers and a number K,
//return which contiguous elements of the list sum to K.
//
//For example, if the list is [1, 2, 3, 4, 5] and K is 9,
//then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

public class DailyCoding102 {

	public static void main(String[] args) {
		
		int[] arr = {1,2,3,4,5};
		int k = 9;
		List list = new ArrayList();
		int sum = 0;
		
		for(int i = 0; i < arr.length; i ++) {
			if(sum == k) break;
			
			sum += arr[i];
			
			if(sum < k){
				list.add(arr[i]);
			}else {
				sum -= (int)list.get(0);
				list.remove(0);
				list.add(arr[i]);
			}
			
		}
		System.out.println(list);
		
		
	}
}

```
