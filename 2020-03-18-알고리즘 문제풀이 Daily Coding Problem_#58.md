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

//양방향 탐색 말하는 건지 모르겠다..
//양방향 탐색이 빠르긴 할것같은데 변환하는 비용 따지면 낭비 같다.
//내일 양방향 탐색 구현해보기 주말에 배열 탐색방법 정리 해보기

public class DailyCoding58 {

	public static void main(String[] args) {
		int n = 6;
		int[] arr = { 13, 18, 25, 2, 8, 10 };
		int find = 8;
		int st = 0;
		int en = arr.length - 1;

		System.out.println(Arrays.asList(arr).get(0));
		
		Arrays.sort(arr);

//		이진 탐색은 정렬해서 인덱스를 찾는 의미가 없음
//		선형 탐색보다 빠르다고 하는것만 보고 이진탐색을 생각 없이 ㅠ
//		System.out.println(binarySearch(find, st, en, arr));
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
