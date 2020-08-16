알고리즘 문제풀이



```java
package DailyCoding;

import java.util.Arrays;

public class DailyCoding60 {

//	 이전 방법은 sort를 하기때문에 {13, 7, 15,5, 5, 25} 같은 배열이 나오면 true를 반환하지만 정상적으로 나누지 않음
//	Given a multiset of integers, return whether it can be partitioned
//	into two subsets whose sums are the same.
//	For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
//	it would return true, 
//	since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, 
//	which both add up to 55.
//	Given the multiset {15, 5, 20, 10, 35}, it would return false, 
//	since we can't split it up into two subsets that add up to the same sum.
// 오류 수정
	public static void main(String[] args) {
		
//		 int[] arr = {15, 5, 20, 10, 35, 15, 10};
		 int[] arr = {13, 7, 15,5, 5, 25};

		 int sum = 0;
		 
		 for(int i = 0; i < arr.length; i ++) {
			 sum += arr[i];
		 }
		 if(check(sum)) {
			 System.out.println(true);
			 print(arr, sum/2, 0);
		 }else {
			 System.out.println(false);
		 }
	}
	
	public static boolean check(int sum) {
		 if((sum / 2)*2 == sum) {
			 return true;
		 }
		 return false;
}
	
	public static void print(int[] arr, int sum, int ck) {
		boolean[] flag = new boolean[arr.length];
		int num = 0;
		int size = 0;
		Arrays.sort(arr);
		
		for(int i = arr.length - 1; i >= 0; i --) {
			if(num + arr[i] <= sum && num + arr[i] != ck) {
				num += arr[i];
				flag[i] = false;
				size ++;
			}else {
				flag[i] = true;
				continue;
			}
		}
		
		if(sum != num) {
			print(arr, sum, num);
			return;
		}
		
		int[] a = new int[arr.length - size];
		int cntA = 0;
		int[] b = new int[size];
		int cntB = 0;
		for(int i = 0; i < arr.length; i ++)	 {
			if(flag[i] == false) {
				b[cntB] = arr[i];
				cntB ++;
			}else {
				a[cntA] = arr[i];
				cntA ++;
			}
		}
		
		System.out.println(Arrays.toString(a) + "          " + Arrays.toString(b));
	}

}


```
