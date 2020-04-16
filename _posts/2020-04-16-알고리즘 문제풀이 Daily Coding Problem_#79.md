알고리즘 문제풀이



```java
package DailyCoding;


//Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
//
//For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
//
//Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

public class DailyCoding79 {
	
	
	public static void main(String[] args) {
		
//		int[] arr = {10,5,7};
		int[] arr = {10,5,1};

	int result = checkArr(arr);
	System.out.println(result == -1?false:result);
	
	}
	
	public static int checkArr(int[] arr) {
		int temp = arr[arr.length - 1];
		int result = 0;
		for(int i = arr.length - 1; i >= 0; i --) {
			if(i > arr[i]) return -1;
			if(temp < arr[i]) {
					result ++;
			}
		}
		return result;
	}
	
}

```

